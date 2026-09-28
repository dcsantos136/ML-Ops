import mlflow
c=mlflow.tracking.MlflowClient()
exps=c.list_experiments()
print('experiments:')
for e in exps:
    print(f"{e.experiment_id}: {e.name}")
    runs = c.search_runs([e.experiment_id])
    for r in runs:
        print('  ', r.info.run_id, r.info.run_name, r.data.metrics.get('accuracy'))
