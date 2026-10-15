
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    "owner": "salil",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}


def execute_step(step_number):
    print(f"Executing Step {step_number}")
    print(f"Step {step_number} completed successfully")


with DAG(
    dag_id="ten_step_dag",
    default_args=default_args,
    description="A DAG with 10 sequential Python tasks",
    start_date=datetime(2026, 1, 1),
    schedule="0 9 * * *",  # Daily at 9 AM
    catchup=False,
    tags=["demo", "10-steps"],
) as dag:

    tasks = []

    for i in range(1, 11):
        task = PythonOperator(
            task_id=f"step_{i}",
            python_callable=execute_step,
            op_args=[i],
        )
        tasks.append(task)

    # Execute all 10 tasks sequentially
    for i in range(len(tasks) - 1):
        tasks[i] >> tasks[i + 1]
