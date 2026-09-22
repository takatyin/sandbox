import numpy as np
import pandas as pd


def validate(model, validation_df: pd.DataFrame) -> float:
    """Evaluate the model with root mean squared error."""
    predictions = np.full(len(validation_df), model["mean_target"], dtype=float)
    targets = validation_df["target"].to_numpy(dtype=float)
    return float(np.sqrt(np.mean((targets - predictions) ** 2)))
