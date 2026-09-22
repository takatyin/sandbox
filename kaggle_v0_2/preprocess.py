from pathlib import Path

import pandas as pd


def resolve_data_dir(data_dir: Path | None = None) -> Path:
    """Resolve the raw-data directory without modifying the existing v0."""
    if data_dir is not None:
        path = Path(data_dir)
        if not path.exists():
            raise FileNotFoundError(f"data directory does not exist: {path}")
        return path

    candidates = (Path("data/raw"), Path("data"), Path("kaggle_v0/data"))
    for path in candidates:
        if (path / "train.csv").exists() and (path / "test.csv").exists():
            return path
    raise FileNotFoundError("Could not find train.csv and test.csv in ./data or ./kaggle_v0/data")


def preprocess(data_dir: Path | None = None):
    """Load, validate, and split the CSV data into train/validation/test frames."""
    raw_dir = resolve_data_dir(data_dir)
    train_df = pd.read_csv(raw_dir / "train.csv")
    test_df = pd.read_csv(raw_dir / "test.csv")

    required_train = {"id", "feature", "target"}
    required_test = {"id", "feature"}
    if not required_train.issubset(train_df.columns):
        raise ValueError(f"train.csv must contain {sorted(required_train)}")
    if not required_test.issubset(test_df.columns):
        raise ValueError(f"test.csv must contain {sorted(required_test)}")
    if len(train_df) < 2:
        raise ValueError("train.csv must contain at least two rows")

    train_df = train_df.loc[:, ["id", "feature", "target"]].copy()
    test_df = test_df.loc[:, ["id", "feature"]].copy()
    for frame, columns in ((train_df, ["feature", "target"]), (test_df, ["feature"])):
        for column in columns:
            frame[column] = pd.to_numeric(frame[column], errors="raise")

    validation_size = max(1, len(train_df) // 5)
    fit_df = train_df.iloc[:-validation_size].reset_index(drop=True)
    validation_df = train_df.iloc[-validation_size:].reset_index(drop=True)
    return fit_df, validation_df, test_df.reset_index(drop=True)
