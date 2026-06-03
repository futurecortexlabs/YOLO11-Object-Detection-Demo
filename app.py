from functools import lru_cache
from pathlib import Path
from urllib.request import urlretrieve

import gradio as gr
import pandas as pd
from PIL import Image
from ultralytics import YOLO


MODEL_NAME = "yolo11n.pt"
MODEL_PATH = Path(MODEL_NAME)
MODEL_URL = (
    "https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt"
)


def download_model_if_needed():
    """モデルファイルがない場合は、初回だけダウンロードします。"""
    if MODEL_PATH.exists():
        return

    print(f"{MODEL_NAME} が見つからないため、モデルをダウンロードします...")
    urlretrieve(MODEL_URL, MODEL_PATH)
    print("モデルのダウンロードが完了しました。")


@lru_cache(maxsize=1)
def load_model():
    """YOLOモデルを一度だけ読み込みます。"""
    download_model_if_needed()
    return YOLO(str(MODEL_PATH))


def create_empty_table():
    """検出結果がない場合にも、表の列をわかりやすく表示します。"""
    return pd.DataFrame(
        columns=[
            "class_name",
            "confidence",
            "x_min",
            "y_min",
            "x_max",
            "y_max",
        ]
    )


def detect_objects(input_image, confidence_threshold, iou_threshold):
    """アップロード画像に対してYOLO11で物体検出を実行します。"""
    if input_image is None:
        return (
            None,
            create_empty_table(),
            "画像が未入力です。左側のアップロード欄から画像を選択してください。",
        )

    try:
        # Gradioから渡された画像をRGB形式に統一します。
        image = Image.fromarray(input_image).convert("RGB")

        model = load_model()
        results = model.predict(
            source=image,
            conf=confidence_threshold,
            iou=iou_threshold,
            verbose=False,
        )

        result = results[0]

        # 検出結果を描画した画像を作成します。
        annotated_image = result.plot()

        detection_rows = []
        boxes = result.boxes

        if boxes is not None and len(boxes) > 0:
            for box in boxes:
                class_id = int(box.cls[0].item())
                class_name = result.names[class_id]
                confidence = float(box.conf[0].item())
                x_min, y_min, x_max, y_max = box.xyxy[0].tolist()

                detection_rows.append(
                    {
                        "class_name": class_name,
                        "confidence": round(confidence, 4),
                        "x_min": round(x_min, 2),
                        "y_min": round(y_min, 2),
                        "x_max": round(x_max, 2),
                        "y_max": round(y_max, 2),
                    }
                )

        detections_df = (
            pd.DataFrame(detection_rows)
            if detection_rows
            else create_empty_table()
        )

        message = (
            f"{len(detection_rows)}件の物体を検出しました。"
            if detection_rows
            else "指定されたしきい値では物体を検出できませんでした。"
        )

        return annotated_image, detections_df, message

    except Exception as error:
        # Spaces上でも原因が見えるように、UIへ短いエラーメッセージを返します。
        return (
            None,
            create_empty_table(),
            f"推論中にエラーが発生しました: {error}",
        )


with gr.Blocks(title="YOLO11 Object Detection Demo") as demo:
    gr.Markdown(
        """
        # YOLO11 物体検出デモ

        画像をアップロードすると、事前学習済みのYOLO11モデルが物体を検出します。
        confidence threshold と IoU threshold を調整して、検出結果の変化を確認できます。
        """
    )

    with gr.Row():
        with gr.Column():
            input_image = gr.Image(
                label="検出したい画像",
                type="numpy",
            )
            confidence_slider = gr.Slider(
                minimum=0.05,
                maximum=1.0,
                value=0.25,
                step=0.05,
                label="Confidence threshold",
            )
            iou_slider = gr.Slider(
                minimum=0.1,
                maximum=1.0,
                value=0.45,
                step=0.05,
                label="IoU threshold",
            )
            detect_button = gr.Button("物体検出を実行", variant="primary")

        with gr.Column():
            output_image = gr.Image(label="検出結果画像")
            status_message = gr.Textbox(
                label="メッセージ",
                value="画像をアップロードして、物体検出を実行してください。",
                interactive=False,
            )

    detections_table = gr.Dataframe(
        headers=["class_name", "confidence", "x_min", "y_min", "x_max", "y_max"],
        label="検出結果テーブル",
        interactive=False,
    )

    detect_button.click(
        fn=detect_objects,
        inputs=[input_image, confidence_slider, iou_slider],
        outputs=[output_image, detections_table, status_message],
    )


if __name__ == "__main__":
    demo.launch()
