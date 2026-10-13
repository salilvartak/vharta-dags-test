import time
from datetime import datetime, timedelta

from airflow import DAG

try:
    from airflow.sdk import BaseOperator, Variable
except ImportError:
    from airflow.models import BaseOperator, Variable

try:
    from airflow.providers.standard.triggers.temporal import TimeDeltaTrigger
except ImportError:
    from airflow.triggers.temporal import TimeDeltaTrigger

from airflow.providers.standard.operators.bash import BashOperator


class WaitForApproval(BaseOperator):
    def execute(self, context):
        self.log.info("DIAG execute started, try_number=%s", context["ti"].try_number)
        flag = Variable.get("approval_demo_approved", default="no")
        self.log.info("DIAG flag=%r", flag)
        time.sleep(45)
        if flag == "yes":
            return "approved"
        self.log.info("DIAG deferring now")
        self.defer(trigger=TimeDeltaTrigger(timedelta(hours=1)), method_name="resume")

    def resume(self, context, event=None):
        return "resumed"


with DAG(
    dag_id="approval_demo",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:
    wait = WaitForApproval(task_id="wait_for_human")
    done = BashOperator(task_id="after_approval", bash_command="echo approved and running")
    wait >> done
