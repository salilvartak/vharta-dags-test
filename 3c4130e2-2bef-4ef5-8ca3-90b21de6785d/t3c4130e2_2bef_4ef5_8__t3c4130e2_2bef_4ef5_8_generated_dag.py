from __future__ import annotations

from datetime import datetime
from airflow.operators.empty import EmptyOperator
from airflow.sdk import dag, task

@dag(
    dag_id="t3c4130e2_2bef_4ef5_8__t3c4130e2_2bef_4ef5_8_generated_dag",
    description="Change the schedule to every 5 minutes and add a notify_done checkpoint after all_healthy.",
    schedule="*/5 * * * *",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["generated"],
)
def t3c4130e2_2bef_4ef5_8__t3c4130e2_2bef_4ef5_8_generated_dag():
    """Change the schedule to every 5 minutes and add a notify_done checkpoint after all_healthy."""

    @task(task_id="all_healthy")
    def all_healthy(**kwargs):
        pass

    @task(task_id="notify_done")
    def notify_done(**kwargs):
        pass
    all_healthy_result = all_healthy()
    notify_done_result = notify_done()
    all_healthy_result >> notify_done_result

t3c4130e2_2bef_4ef5_8__t3c4130e2_2bef_4ef5_8_generated_dag_dag = t3c4130e2_2bef_4ef5_8__t3c4130e2_2bef_4ef5_8_generated_dag()
