# AI Sentiment Analysis MLOps Project

End-to-end MLOps pipeline for sentiment analysis using Machine Learning, DVC, MLflow, Flask, Docker, Kubernetes, Terraform and GitHub Actions.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-WebApp-black)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![MLflow](https://img.shields.io/badge/MLflow-Experiment%20Tracking-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Project Structure](#project-structure)
4. [Tech Stack](#tech-stack)
5. [Dataset](#dataset)
6. [Machine Learning Pipeline](#machine-learning-pipeline)
7. [DVC Pipeline](#dvc-pipeline)
8. [MLflow Experiment Tracking](#mlflow-experiment-tracking)
9. [Model Performance](#model-performance)
10. [Flask Web Application](#flask-web-application)
11. [Docker Deployment](#docker-deployment)
12. [Kubernetes Deployment](#kubernetes-deployment)
13. [Terraform Infrastructure](#terraform-infrastructure)
14. [CI/CD Pipeline](#cicd-pipeline)
15. [Testing](#testing)
16. [Installation](#installation)
17. [Running the Project](#running-the-project)
18. [Future Enhancements](#future-enhancements)
19. [Author](#author)

---

## Project Overview

This project predicts whether a given text review expresses a **Positive** or **Negative** sentiment.

It demonstrates a complete, production-style MLOps workflow covering the full lifecycle of a machine learning system:

- Data Ingestion
- Data Preprocessing
- Feature Engineering
- Model Training
- Model Evaluation
- Experiment Tracking with MLflow
- Data Versioning using DVC
- Flask Deployment
- Docker Containerization
- Kubernetes Deployment
- Terraform Infrastructure Provisioning
- CI/CD using GitHub Actions

The goal of this project is to showcase practical MLOps engineering skills, bridging cloud infrastructure, automation, and applied data science.

---

## System Architecture

<img width="1024" height="1536" alt="Copilot_20260630_195427" src="https://github.com/user-attachments/assets/57077295-d8a3-4aec-bb16-9bc1282e9a43" />


```
Raw Data
   ↓
Preprocessing
   ↓
Feature Engineering
   ↓
Model Training
   ↓
MLflow Tracking
   ↓
Model Registry
   ↓
Flask API
   ↓
Docker
   ↓
Kubernetes
```

---

## Project Structure

```
sentiment-analysis-mlops/
├── data/
│   ├── raw/
│   ├── processed/
│   └── features/
├── src/
│   ├── data/
│   │   ├── data_ingestion.py
│   │   └── data_preprocessing.py
│   ├── features/
│   │   └── feature_engineering.py
│   └── model/
│       ├── train_model.py
│       ├── model_evaluation.py
│       └── register_model.py
├── flask_app/
│   ├── app.py
│   ├── templates/
│   └── static/
├── tests/
│   ├── test_model.py
│   └── test_flask_app.py
├── k8s/
│   └── deployment.yaml
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── .github/
│   └── workflows/
│       └── ci-cd.yaml
├── screenshots/
├── dvc.yaml
├── params.yaml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Tech Stack

| Category | Technology |
|---|---|
| Language | Python |
| ML | Scikit-Learn |
| Tracking | MLflow |
| Versioning | DVC |
| Web App | Flask |
| Containerization | Docker |
| Orchestration | Kubernetes |
| IaC | Terraform |
| CI/CD | GitHub Actions |
| Testing | Pytest |
| Cloud | AWS |

---

## Dataset

**Dataset:** IMDB Movie Reviews

**Classes:**
- Positive
- Negative

| Split | Samples |
|---|---|
| Training | xxxx |
| Testing | xxxx |

---

## Machine Learning Pipeline

| Stage | File |
|---|---|
| Data Ingestion | `src/data/data_ingestion.py` |
| Data Preprocessing | `src/data/data_preprocessing.py` |
| Feature Engineering | `src/features/feature_engineering.py` |
| Model Training | `src/model/train_model.py` |
| Model Evaluation | `src/model/model_evaluation.py` |
| Model Registration | `src/model/register_model.py` |

---

## DVC Pipeline

![DVC Pipeline](screenshots/dvc_pipeline.png)

Reproduce the full pipeline:

```bash
dvc repro
```

Visualize the pipeline DAG:

```bash
dvc dag
```

---

## MLflow Experiment Tracking

<img width="1907" height="1015" alt="mlflow_exps" src="https://github.com/user-attachments/assets/9abbc695-57b9-4ab8-afd0-4b325c79f219" />
<img width="1875" height="1012" alt="mlo4" src="https://github.com/user-attachments/assets/4b43d8e7-b93c-4328-a7dd-36f25b030a55" />
<img width="1877" height="985" alt="mlflow3" src="https://github.com/user-attachments/assets/151bafb5-e794-4914-8cb4-12356c302dd5" />
<img width="1917" height="1020" alt="mlflow2" src="https://github.com/user-attachments/assets/504f88dd-e788-4324-993a-49c863d9ba54" />
<img width="1910" height="1010" alt="mlflow_models" src="https://github.com/user-attachments/assets/09552005-50ca-4c00-90f6-5776390970ad" />


MLflow is used to track:

- Parameters
- Metrics
- Artifacts
- Model Registry

Launch the MLflow UI:

```bash
mlflow ui
```

---

## Model Performance

| Metric | Score |
|---|---|
| Accuracy | xx% |
| Precision | xx% |
| Recall | xx% |
| F1 Score | xx% |

---

## Flask Web Application




### Positive Prediction
<img width="1917" height="1017" alt="positive_sentiment" src="https://github.com/user-attachments/assets/cb4e9dc8-5e2b-44ad-b722-b96685691924" />

### Negative Prediction
<img width="1915" height="1017" alt="negative_sentiment" src="https://github.com/user-attachments/assets/3feec371-eea5-44d5-a270-0ec3d1dbdfb5" />


---

## Docker Deployment

Build the image:

```bash
docker build -t sentiment-analysis .
```

Run the container:

```bash
docker run -p 5000:5000 sentiment-analysis
```

---

## Kubernetes Deployment

<img width="1917" height="1021" alt="runningpods" src="https://github.com/user-attachments/assets/467187ff-93e4-4cc9-a07b-d06ed2e088b3" />


Apply the deployment:

```bash
kubectl apply -f k8s/deployment.yaml
```

Check pod status:

```bash
kubectl get pods
```

---

## Terraform Infrastructure

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

---

## CI/CD Pipeline

![CI/CD](screenshots/github_actions.png)

The GitHub Actions workflow includes:

- Unit Tests
- Code Validation
- Docker Build
- Deployment

---

## Testing

Run the test suite:

```bash
pytest tests/
```

Available tests:

- `test_model.py`
- `test_flask_app.py`

---

## Installation

Clone the repository:

```bash
git clone <repo-url>
cd sentiment-analysis-mlops
```

Create a virtual environment:

```bash
conda create -n sentiment python=3.10
conda activate sentiment
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Train the model:

```bash
python src/model/train_model.py
```

Run the Flask app:

```bash
python flask_app/app.py
```

Open in your browser:

```
http://loadbalancerservicefromclusterip:5000
```

---

## Future Enhancements

- FastAPI Deployment
- AWS EKS Deployment
- Model Drift Detection
- Monitoring using Prometheus & Grafana
- Automated Retraining
- LLM-based Sentiment Analysis

---

## Author

**Shakeer Mohammed**

- Email: mds.shakeer@gmail.com
- GitHub: [shakeer7](https://github.com/shakeer7)

---

## License

This project is licensed under the MIT License.
