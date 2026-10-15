
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    "owner": "salil",
    "retries": 2,
    "retry_delay": timedelta(minutes=1),
}


def extract_data():
    print("Step 1: Extracting data from source")


def validate_data():
    print("Step 2: Validating extracted data")


def clean_data():
    print("Step 3: Cleaning invalid records")


def transform_data():
    print("Step 4: Transforming data")


def enrich_data():
    print("Step 5: Enriching data with additional fields")


def process_data():
    print("Step 6: Processing business logic")


def analyze_data():
    print("Step 7: Analyzing processed data")


def generate_report():
    print("Step 8: Generating report")


def save_results():
    print("Step 9: Saving results")


def notify_completion():
    print("Step 10: Pipeline completed successfully")


with DAG(
    dag_id="data_processing_dag",
    default_args=default_args,
    description="10-step data processing pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="0 */6 * * *",
    catchup=False,
    tags=["data-processing", "pipeline"],
) as dag:

    step_1 = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data,
    )

    step_2 = PythonOperator(
        task_id="validate_data",
        python_callable=validate_data,
    )

    step_3 = PythonOperator(
        task_id="clean_data",
        python_callable=clean_data,
    )

    step_4 = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data,
    )

    step_5 = PythonOperator(
        task_id="enrich_data",
        python_callable=enrich_data,
    )

    step_6 = PythonOperator(
        task_id="process_data",
        python_callable=process_data,
    )

    step_7 = PythonOperator(
        task_id="analyze_data",
        python_callable=analyze_data,
    )

    step_8 = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report,
    )

    step_9 = PythonOperator(
        task_id="save_results",
        python_callable=save_results,
    )

    step_10 = PythonOperator(
        task_id="notify_completion",
        python_callable=notify_completion,
    )

    (
        step_1
        >> step_2
        >> step_3
        >> step_4
        >> step_5
        >> step_6
        >> step_7
        >> step_8
        >> step_9
        >> step_10
    )
