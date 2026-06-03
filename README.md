# YOLO11 Object Detection Demo

画像をアップロードすると、事前学習済みYOLO11モデルで物体検出を行うWebデモです。Python、Gradio、Ultralytics YOLOを使い、GitHubとHugging Face Spacesで公開しやすい構成にしています。

## できること

- 画像アップロードによる物体検出
- 検出結果を描画した画像の表示
- 検出したクラス名、信頼度、バウンディングボックス座標の表表示
- confidence threshold の調整
- IoU threshold の調整
- Hugging Face SpacesでのWeb公開

## 使っている技術

- Python
- Gradio
- Ultralytics YOLO
- YOLO11n事前学習済みモデル
- pandas
- Pillow

## ローカル実行方法

```bash
git clone https://github.com/your-name/YOLO-Object-Detection-Demo.git
cd YOLO-Object-Detection-Demo
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

## Hugging Face Spacesでの公開方法

1. Hugging Faceにログインします。
2. 右上のメニューから「New Space」を作成します。
3. Space SDKは「Gradio」を選択します。
4. リポジトリに以下のファイルをアップロードします。
   - `app.py`
   - `requirements.txt`
   - `README.md`
   - `.gitignore`
   - `sample_images/`
   - `docs/`
5. Spaceが自動で依存関係をインストールし、`app.py` を起動します。
6. 画面が表示されたら、画像をアップロードして物体検出を試します。

## GitHub公開時の説明

このリポジトリは、YOLO11を使った画像アップロード型の物体検出デモです。学習は行わず、事前学習済みモデル `yolo11n.pt` による推論のみを実行します。

ポートフォリオでは、次のような観点を説明できます。

- Gradioによるシンプルな機械学習Web UIの作成
- Ultralytics YOLOによる物体検出推論
- 推論結果の画像描画と表形式での可視化
- confidence thresholdとIoU thresholdによる検出条件の調整
- Hugging Face Spacesを使ったAIデモの公開

## 今後の発展案

このデモは、画像AIアプリケーションの基礎として発展させることができます。

- 製品画像から傷や欠けを見つけるAI画像検査
- 工場ライン向けの異常検知デモ
- カメラ画像を使ったリアルタイム検査
- 検出ログの保存と分析
- 独自データで追加学習した検査モデルへの拡張

今回はMVTec ADなどの外部データセットは使わず、学習も行いません。事前学習済みYOLOモデルによる推論のみを扱います。
