import json
import warnings

import mlflow
import dagshub

from src.logger import logging

warnings.filterwarnings("ignore")


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
def load_model_info(file_path: str) -> dict:
    """
    Load experiment information from JSON file.
    """
    try:
        with open(file_path, "r") as f:
            model_info = json.load(f)

        logging.info("Model info loaded successfully")
        return model_info

    except Exception as e:
        logging.error("Failed to load model info: %s", e)
        raise


def register_model(model_name: str, model_info: dict):
    """
    Register model in MLflow Model Registry.
    """

    try:
        run_id = model_info["run_id"]

        # MLflow model artifact location
        model_uri = f"runs:/{run_id}/model"

        print(f"Model URI: {model_uri}")

        registered_model = mlflow.register_model(
            model_uri=model_uri,
            name=model_name
        )

        print(
            f"Registered Model: {model_name}, "
            f"Version: {registered_model.version}"
        )

        logging.info(
            "Model %s registered successfully. Version %s",
            model_name,
            registered_model.version
        )

    except Exception as e:
        logging.error(
            "Model registration failed: %s",
            e
        )
        raise


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main():

    try:

        model_info = load_model_info(
            "reports/experiment_info.json"
        )

        register_model(
            model_name="sentiment_model",
            model_info=model_info
        )

        print("Model registration completed.")

    except Exception as e:

        logging.error(
            "Failed to complete model registration: %s",
            e
        )

        print(f"Error: {e}")


if __name__ == "__main__":
    main()