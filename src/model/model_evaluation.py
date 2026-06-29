import numpy as np
import pandas as pd
import pickle
import json
import mlflow
import mlflow.sklearn
import dagshub

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    roc_auc_score
)

from src.logger import logging


# -----------------------------------------------------------------------------
# MLflow + DagsHub Setup
# -----------------------------------------------------------------------------
mlflow.set_tracking_uri(
    "https://dagshub.com/mds.shakeer/mlops_sentiments_analysis.mlflow"
)

dagshub.init(
    repo_owner="mds.shakeer",
    repo_name="mlops_sentiments_analysis",
    mlflow=True
)


# -----------------------------------------------------------------------------
# Utility Functions
# -----------------------------------------------------------------------------
def load_model(file_path):
    with open(file_path, "rb") as f:
        model = pickle.load(f)

    logging.info("Model loaded successfully")
    return model


def load_data(file_path):
    df = pd.read_csv(file_path)

    logging.info("Data loaded successfully")
    return df


def evaluate_model(model, X_test, y_test):

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "auc": roc_auc_score(y_test, y_prob)
    }

    return metrics


def save_metrics(metrics, file_path):

    with open(file_path, "w") as f:
        json.dump(metrics, f, indent=4)

    logging.info("Metrics saved")


def save_model_info(run_id, file_path):

    model_info = {
        "run_id": run_id,
        "model_path": "model"
    }

    with open(file_path, "w") as f:
        json.dump(model_info, f, indent=4)

    logging.info("Experiment info saved")


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main():

    mlflow.set_experiment("sentiment-pipeline-v3")

    with mlflow.start_run() as run:

        try:

            clf = load_model("./models/model.pkl")

            test_data = load_data(
                "./data/processed/test_bow.csv"
            )

            X_test = test_data.iloc[:, :-1].values
            y_test = test_data.iloc[:, -1].values

            metrics = evaluate_model(
                clf,
                X_test,
                y_test
            )

            save_metrics(
                metrics,
                "reports/metrics.json"
            )

            # Log Metrics
            mlflow.log_metrics(metrics)

            # Log Parameters
            mlflow.log_params(clf.get_params())

            # Log Model
            model_info = mlflow.sklearn.log_model(
                sk_model=clf,
                name="model"
            )

            print(model_info)

            # Save Run Info
            save_model_info(
                run.info.run_id,
                "reports/experiment_info.json"
            )

            # Log Artifact
            mlflow.log_artifact(
                "reports/metrics.json"
            )

            print(
                f"Run ID: {run.info.run_id}"
            )

            logging.info(
                "Model evaluation completed successfully"
            )

        except Exception as e:

            logging.error(
                f"Model evaluation failed: {e}"
            )

            raise


if __name__ == "__main__":
    main()