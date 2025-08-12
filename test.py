import mlflow

exp_id = mlflow.create_experiment('test')

print(exp_id)