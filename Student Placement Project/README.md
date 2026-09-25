# Student Placement Project

This repository contains an end-to-end machine learning project for predicting student placement outcomes. It includes data preprocessing, feature engineering, model training, evaluation, and a minimal API and frontend for serving predictions.

## Project Structure

- `data/` - raw and processed datasets
- `dags/` - Airflow DAGs for pipeline orchestration
- `src/` - main source code
  - `src/data/` - dataset creation utilities
  - `src/features/` - feature engineering
  - `src/models/` - model training and inference
  - `src/api.py` - simple prediction API
  - `src/frontend/` - minimal frontend for demo
- `mlruns/` - MLflow run artifacts and model registry
- `reports/` - generated reports and figures

## Setup

Create a Python virtual environment and install dependencies:

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Run tests and environment checks:

```powershell
python -m pytest
python test_environment.py
```

## Usage

- Prepare data: implement or run `src/data/make_dataset.py` to generate processed datasets from `data/raw/`.
- Train a model: use `src/models/train_model.py` to train and log models with MLflow.
- Evaluate: run `src/evaluate_model.py` for evaluation metrics and plots.
- Serve predictions: start the API defined in `src/api.py` (e.g., with `uvicorn src.api:app --reload`).

## Development

- Code style and tests are managed via `tox.ini` and `setup.py`.
- Use `Makefile` targets or direct Python scripts for common tasks.

## Notes

- Data included under `data/raw/` is a sample CSV (`student_placement_data_v1.csv`).
- Experiment tracking is stored in `mlruns/` (MLflow).

## License

See `LICENSE` for license details.

---
Generated README for quick project onboarding. Update any sections as needed.
Student-Project
==============================

A short description of the project.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
