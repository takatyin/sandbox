def train(train_data):
    """Train a naive baseline that always predicts the training target mean."""
    mean_target = sum(row["target"] for row in train_data) / len(train_data)
    return {"mean_target": mean_target}
