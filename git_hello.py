with DAG(
    dag_id="daily_scheduled_dag",
    start_date=pendulum.datetime(2026, 10, 14, tz="Asia/Kolkata"),
    schedule="0 0 * * *",
    catchup=False,
) as dag:
    start = EmptyOperator(task_id="start")
    finish = EmptyOperator(task_id="finish")

    start >> finish
