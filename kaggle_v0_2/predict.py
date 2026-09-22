import numpy as np
import pandas as pd


def predict(model, test_df: pd.DataFrame) -> pd.DataFrame:
    """Create predictions while preserving the test row order and ids."""
    return pd.DataFrame(
        {
            "id": test_df["id"].to_numpy(),
            "prediction": np.full(len(test_df), model["mean_target"], dtype=float),
        }
    )
