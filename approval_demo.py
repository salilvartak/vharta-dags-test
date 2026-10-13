from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.sensors.time_delta import TimeDeltaSensor

with DAG(
    dag_id="approval_demo",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:
    wait = TimeDeltaSensor(
        task_id="wait_for_human",
        delta=timedelta(hours=1),
        deferrable=True,
    )
    done = BashOperator(task_id="after_approval", bash_command="echo approved and running")
    wait >> done
