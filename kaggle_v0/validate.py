import math


def validate(trained_model, val_data):
    """Return root mean squared error on the validation data."""
    prediction = trained_model["mean_target"]
    squared_errors = [
        (row["target"] - prediction) ** 2
        for row in val_data
    ]
    return math.sqrt(sum(squared_errors) / len(squared_errors))
