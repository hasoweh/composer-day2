from airflow import models

with models.DAG(
    "first_dag",
    schedule_interval=datetime.timedelta(weeks=4)
) as dag:

    # Create BigQuery output dataset.
    make_bq_dataset = bash.BashOperator(
        task_id="make_bq_dataset",
        # Executing 'bq' command requires Google Cloud SDK which comes
        # preinstalled in Cloud Composer.
        bash_command="echo $(gcloud secrets versions access latest --secret='my-secret')",
    )