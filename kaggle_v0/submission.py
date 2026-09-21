import csv
from pathlib import Path


def make_submission(predictions, output_path=Path("submission.csv")):
    """Write predictions in submission format and return the output path."""
    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "prediction"])
        writer.writeheader()
        writer.writerows(predictions)
    return output_path
