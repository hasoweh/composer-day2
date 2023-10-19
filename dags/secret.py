from airflow import models
import datetime
from airflow.operators import bash

default_dag_args = {
    "start_date": datetime.datetime(2023, 10, 1),
    "retries": 1,
    "retry_delay": datetime.timedelta(minutes=5)
}

with models.DAG(
    "secret_dag",
    default_args=default_dag_args,
    schedule_interval=datetime.timedelta(weeks=4)
) as dag:

    # Create BigQuery output dataset.
    make_bq_dataset = bash.BashOperator(
        task_id="make_bq_dataset",
        # Executing 'bq' command requires Google Cloud SDK which comes
        # preinstalled in Cloud Composer.
        bash_command="echo $(gcloud secrets versions access latest --secret='my-secret')",
    )