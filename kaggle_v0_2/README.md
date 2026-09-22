# Kaggle experiment v0.2

`kaggle_v0` を変更せず、指示書の1回分の実験ループを別ディレクトリに実装したものです。

```bash
python3 run_v0_2.py
```

処理は `preprocess`、`train`、`validate`、`predict`、`submission` に分離しています。
データは `./data/raw`、`./data`、`./kaggle_v0/data` の順に探索します。
モデルは学習データの `target` 平均値を予測するnaive baselineで、検証指標はRMSEです。
