FROM apache/airflow:2.11.2-python3.12

ARG AIRFLOW_VERSION=2.11.2

COPY requirements-airflow.txt /requirements-airflow.txt
RUN pip install --no-cache-dir \
    "apache-airflow==${AIRFLOW_VERSION}" \
    -r /requirements-airflow.txt \
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-3.12.txt"

COPY --chown=airflow:root dags/ /opt/airflow/dags/
COPY --chown=airflow:root src/ /opt/airflow/src/

ENV AIRFLOW__CORE__DAGS_FOLDER=/opt/airflow/dags \
    AIRFLOW__CORE__LOAD_EXAMPLES=False \
    PYTHONPATH=/opt/airflow

CMD ["standalone"]
