---
title: YOLO11 Object Detection Demo
emoji: 🖼️
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "5.33.0"
python_version: "3.10"
app_file: app.py
pinned: false
---

# YOLO11 Object Detection Demo

画像をアップロードすると、事前学習済みYOLO11モデルで物体検出を行うWebデモです。

## できること

- 画像アップロードによる物体検出
- 検出結果を描画した画像の表示
- 検出したクラス名、信頼度、バウンディングボックス座標の表表示
- confidence threshold の調整
- IoU threshold の調整

## 使っている技術

- Python
- Gradio
- Ultralytics YOLO
- YOLO11n事前学習済みモデル
- pandas
- Pillow

## ローカル実行方法

```bash
git clone https://github.com/futurecortexlabs/YOLO11-Object-Detection-Demo.git
cd YOLO11-Object-Detection-Demo
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Windows PowerShellの場合は、仮想環境の有効化コマンドを次のように実行します。

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

起動後、ブラウザで表示されたローカルURLを開きます。

PyTorch 2.6以降が入っている環境で重み読み込みエラーが出る場合は、次のコマンドで依存関係を入れ直してください。

```powershell
pip install --upgrade --force-reinstall -r requirements.txt
```

## 今後の発展案

このデモは、画像AIアプリケーションの基礎として発展させることができます。

- 製品画像から傷や欠けを見つけるAI画像検査
- 工場ライン向けの異常検知デモ
- カメラ画像を使ったリアルタイム検査
- 検出ログの保存と分析
- 独自データで追加学習した検査モデルへの拡張

今回はMVTec ADなどの外部データセットは使わず、学習も行いません。事前学習済みYOLOモデルによる推論のみを扱います。
