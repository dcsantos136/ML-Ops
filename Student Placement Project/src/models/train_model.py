""" Updating the model script for the student placement prediction project for MLFlow tracking ."""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from pathlib import Path

import mlflow
import mlflow.sklearn


def train():
    project_root = Path(__file__).resolve().parents[2]

    df = pd.read_csv(project_root / "data" / "raw" / "student_placement_data.csv")
    X = df.drop("Placement", axis=1)
    y = df["Placement"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    mlflow_db_path = str(project_root / "mlflow.db").replace("\\", "/")
    mlflow.set_tracking_uri(f"sqlite:///{mlflow_db_path}")
    mlflow.set_experiment("Student Placement Prediction")

    configs = [
        {"name": "rf_default", "n_estimators": 100, "max_depth": None, "random_state": 42},
        {"name": "rf_deeper", "n_estimators": 200, "max_depth": 10, "random_state": 42},
        {"name": "rf_small", "n_estimators": 50, "max_depth": 5, "random_state": 42},
    ]

    models_dir = project_root / "models"
    models_dir.mkdir(parents=True, exist_ok=True)

    best_model = None
    best_model_name = None
    best_accuracy = -float("inf")

    for cfg in configs:
        with mlflow.start_run(run_name=cfg["name"]):
            model = RandomForestClassifier(
                n_estimators=cfg["n_estimators"],
                max_depth=cfg["max_depth"],
                random_state=cfg["random_state"],
            )
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)

            mlflow.log_param("model_type", "RandomForestClassifier")
            mlflow.log_params({k: v for k, v in cfg.items() if k != "name"})
            mlflow.log_metric("accuracy", accuracy)

            local_model_path = models_dir / f"model_{cfg['name']}.pkl"
            joblib.dump(model, local_model_path)

            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_model = model
                best_model_name = cfg["name"]

            mlflow.sklearn.log_model(
                model,
                "model",
                skops_trusted_types=["sklearn.tree._tree.Tree"],
            )

            print(f"Run '{cfg['name']}' finished. Accuracy: {accuracy}")

    if best_model is not None:
        canonical_model_path = models_dir / "model.pkl"
        joblib.dump(best_model, canonical_model_path)
        print(
            f"Best model selected: '{best_model_name}' with accuracy {best_accuracy:.4f} "
            f"saved to {canonical_model_path}"
        )


if __name__ == "__main__":
    train()