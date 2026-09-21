from pathlib import Path

from kaggle_v0.predict import predict
from kaggle_v0.preprocess import preprocess
from kaggle_v0.submission import make_submission
from kaggle_v0.train import train
from kaggle_v0.validate import validate


def main():
    train_data, val_data, test_data = preprocess(Path("data/raw"))
    trained_model = train(train_data)
    score = validate(trained_model, val_data)
    predictions = predict(trained_model, test_data)
    submission_path = make_submission(predictions)

    print(f"validation RMSE: {score:.6f}")
    print(f"created: {submission_path}")


if __name__ == "__main__":
    main()
