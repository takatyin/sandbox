# Implementation Prompt

## 1. Goal

Kaggleのv0として、まずは1回の実験ループを実行できる状態にする。

## 2. Current Context

- trainデータは `id`、`feature`、`target` を持つ。
- testデータは `id`、`feature` を持つ。
- submissionは `id`、`prediction` を持つ。
- 既存ディレクトリには、`preprocess`、`train`、`validate`、`predict`、`submission` に対応するファイルが存在する。
- 既存ディレクトリの構成は、できるだけ変更しない。

## 3. Fixed Decisions

- 処理を以下の段階に分ける。
  - preprocess
  - train
  - validate
  - predict
  - submission
- 今回の目的は、まず1回実験ループを回すことである。

## 4. Requirements

- trainデータを入力として、前処理、学習、検証を実行できるようにする。
- testデータを入力として、予測を実行できるようにする。
- `id` と予測値を用いてsubmissionを作成できるようにする。
- 各処理を `preprocess`、`train`、`validate`、`predict`、`submission` の単位に分ける。
- 1回の実験ループを実行できるようにする。
- 使用するモデル、前処理の具体的内容、実験ループの実行方法は `[未決定]`だができるだけnaiveに。
-　検証方法についてまずはE2Eでおこないます、
その後各モジュールにおいてunitテストを行えるような構造の作成をお願いします。(unit testの内部実装はv0では行わない)


## 5. Constraints / Non-goals

- 共通化は行わない。
- loggingは実装しない。
- HPOは実装しない。
- 既存ディレクトリを大きく変更しない。
- 上記以外の制約・non-goalは `[未決定]`。

## 6. Acceptance Criteria

- trainデータの `id`、`feature`、`target` を前提に、preprocessからvalidateまでの処理を1回実行できる。
- testデータの `id`、`feature` を前提に、predictを1回実行できる。
- `id`、`prediction` の形式でsubmissionを作成できる。
- preprocess、train、validate、predict、submissionの処理が分かれている。
- 既存ディレクトリへの変更が必要最小限である。
- 期待するスコア、予測値の詳細仕様は `[未決定]`。
- 評価指標はRMSEで行う。

## 7. Scope of Change

- 対象は、Kaggle v0の1回分の実験ループを動かすために必要な範囲とする。
- 既存の `preprocess`、`train`、`validate`、`predict`、`submission` に対応する構成を必要に応じて更新する。
- 実験ループの起動に必要なファイルや処理は、既存ディレクトリ構成を維持できる範囲で追加・更新する。
- 共通化、logging、HPO、複数実験への対応はスコープ外とする。
- モデル、データの読み込み方法、成果物の保存場所は `[未決定]`。
- ライブラリについてはpandas, numpy, matplotlibを使ってください。

## 8. After Implementation

- 1回の実験ループを実行し、処理が完了することを確認する。
- 作成されたsubmissionを確認する。
- 実行結果の報告内容・形式は `[未決定]`。
