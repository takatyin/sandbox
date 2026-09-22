from pathlib import Path

import matplotlib.pyplot as plt

from .predict import predict
from .preprocess import preprocess
from .submission import make_submission
from .train import train
from .validate import validate


def main(data_dir: Path | None = None):
    fit_df, validation_df, test_df = preprocess(data_dir)
    model = train(fit_df)
    score = validate(model, validation_df)
    predictions = predict(model, test_df)

    plot_path = Path("kaggle_v0_2/validation.png")
    plt.figure(figsize=(5, 3))
    plt.scatter(validation_df["target"], [model["mean_target"]] * len(validation_df))
    plt.xlabel("target")
    plt.ylabel("prediction")
    plt.title(f"Validation RMSE: {score:.4f}")
    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close()

    submission_path = make_submission(predictions)
    print(f"validation RMSE: {score:.6f}")
    print(f"created: {submission_path}")
    print(f"created: {plot_path}")
    return score, submission_path


if __name__ == "__main__":
    main()
