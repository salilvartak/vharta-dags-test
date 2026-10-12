from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="git_hello",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:
    BashOperator(task_id="hello", bash_command="echo hello from git; sleep 60")
