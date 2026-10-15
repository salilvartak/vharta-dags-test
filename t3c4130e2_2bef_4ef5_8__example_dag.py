from __future__ import annotations

from datetime import datetime
from airflow.operators.empty import EmptyOperator
from airflow.sdk import dag, task

@dag(
    dag_id="t3c4130e2_2bef_4ef5_8__example_dag",
    description="write a example Dag",
    schedule="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["example"],
)
def t3c4130e2_2bef_4ef5_8__example_dag():
    """write a example Dag"""

    @task(task_id="start")
    def start(**kwargs):
        pass

    @task(task_id="end")
    def end(**kwargs):
        pass
    start_result = start()
    end_result = end()
    start_result >> end_result

t3c4130e2_2bef_4ef5_8__example_dag_dag = t3c4130e2_2bef_4ef5_8__example_dag()
