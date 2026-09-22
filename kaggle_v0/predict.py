def predict(trained_model, test_data):
    """Create one prediction associated with each test row id."""
    return [
        {"id": row["id"], "prediction": trained_model["mean_target"]}
        for row in test_data
    ]


def predict2(trained_model, test_data):
    pass


