#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${HOME}/.venvs/student-placement-airflow"

if [[ ! -x "${VENV_DIR}/bin/airflow" ]]; then
  echo "Airflow is not installed at ${VENV_DIR}." >&2
  echo "Install it in WSL with the project's documented setup first." >&2
  exit 1
fi

export PATH="${VENV_DIR}/bin:${PATH}"
export AIRFLOW_HOME="${HOME}/.local/share/student-placement-airflow"
export AIRFLOW__CORE__DAGS_FOLDER="${PROJECT_ROOT}/dags"
export AIRFLOW__CORE__LOAD_EXAMPLES=False
export PYTHONPATH="${PROJECT_ROOT}${PYTHONPATH:+:${PYTHONPATH}}"

exec airflow standalone
