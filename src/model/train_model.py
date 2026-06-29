from mlflow.tracking import MlflowClient
import mlflow
import os

# dagshub_token = os.getenv("CAPSTONE_TEST")

# os.environ["MLFLOW_TRACKING_USERNAME"] = dagshub_token
# os.environ["MLFLOW_TRACKING_PASSWORD"] = dagshub_token

mlflow.set_tracking_uri(
    "https://dagshub.com/mds.shakeer/mlops_sentiments_analysis.mlflow"
)

client = MlflowClient()

artifacts = client.list_artifacts(
    "3fb81a9ed0634705962cce09d43779bc"
)

for artifact in artifacts:
    print(artifact.path)