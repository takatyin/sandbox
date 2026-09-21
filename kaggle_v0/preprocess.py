import csv
from pathlib import Path


def preprocess(raw_data: Path):
    """Load raw CSV files and split labeled rows into train and validation data."""
    with (raw_data / "train.csv").open(newline="", encoding="utf-8") as file:
        labeled_rows = list(csv.DictReader(file))

    with (raw_data / "test.csv").open(newline="", encoding="utf-8") as file:
        test_data = list(csv.DictReader(file))

    if len(labeled_rows) < 2:
        raise ValueError("train.csv must contain at least two rows")
    if "target" not in labeled_rows[0]:
        raise ValueError("train.csv must contain a 'target' column")
    if test_data and "id" not in test_data[0]:
        raise ValueError("test.csv must contain an 'id' column")

    for row in labeled_rows:
        row["target"] = float(row["target"])

    validation_size = max(1, len(labeled_rows) // 5)
    train_data = labeled_rows[:-validation_size]
    val_data = labeled_rows[-validation_size:]
    return train_data, val_data, test_data
