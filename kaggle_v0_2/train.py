import numpy as np
import pandas as pd


def train(train_df: pd.DataFrame):
    """Fit the v0 naive baseline: always predict the training target mean."""
    if train_df.empty:
        raise ValueError("cannot train on an empty dataframe")
    return {"mean_target": float(np.mean(train_df["target"].to_numpy(dtype=float)))}
