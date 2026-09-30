from __future__ import annotations

from datetime import datetime
import os
import sys

from airflow import DAG
from airflow.operators.python import PythonOperator

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from src.data_preprocessing import preprocess_data
from src.evaluate_model import evaluate
from src.train_model import train


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "start_date": datetime(2024, 1, 1),
}

with DAG(
    dag_id="ml_pipeline",
    default_args=default_args,
    schedule="@daily",
    catchup=False,
    tags=["ml", "student-placement"],
) as dag:
    preprocess = PythonOperator(
        task_id="data_preprocessing",
        python_callable=preprocess_data,
    )

    train_model = PythonOperator(
        task_id="model_training",
        python_callable=train,
    )

    evaluate_model = PythonOperator(
        task_id="model_evaluation",
        python_callable=evaluate,
    )

    preprocess >> train_model >> evaluate_model