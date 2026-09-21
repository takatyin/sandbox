# Kaggle experiment v0

Raw CSVから`submission.csv`までを一度通すための最小構成です。Python標準ライブラリだけで動作します。

```bash
python3 run.py
```

処理は次のファイルに分離しています。

- `kaggle_v0/preprocess.py`: CSVの読み込みとtrain/validation分割
- `kaggle_v0/train.py`: 目的変数の平均値を学習するbaseline
- `kaggle_v0/validate.py`: RMSEによる検証
- `kaggle_v0/predict.py`: test dataの予測
- `kaggle_v0/submission.py`: `submission.csv`の作成

入力形式は、`data/raw/train.csv`に`target`列、`data/raw/test.csv`に`id`列があることを前提とします。実際のコンペに合わせる際は、まず各処理の対応ファイルだけを差し替えてください。
