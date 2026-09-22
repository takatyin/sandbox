from pathlib import Path

import pandas as pd


def make_submission(predictions: pd.DataFrame, output_path: Path = Path("kaggle_v0_2/submission.csv")) -> Path:
    """Write exactly the required ``id,prediction`` submission columns."""
    required = ["id", "prediction"]
    if list(predictions.columns) != required:
        raise ValueError(f"predictions must have columns {required}")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    predictions.to_csv(output_path, index=False)
    return output_path
