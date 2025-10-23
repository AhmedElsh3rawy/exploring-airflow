# create requirements.txt and put the packages you want to install for example pandas and numpy
# put (_PIP_ADDITIONAL_REQUIREMENTS=pandas numpy) in the .env file and make sure to list your packages separated by space

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {"owner": "ahmed", "retries": 5, "retry_delay": timedelta(minutes=2)}


def get_versions():
    import pandas as pd
    import numpy as np

    print(f"pandas version: {pd.__version__}")
    print(f"numpy version: {np.__version__}")


with DAG(
    dag_id="dag_with_extended_packages",
    default_args=default_args,
    start_date=datetime(2023, 4, 10, 2),
    schedule="@daily",
) as dag:
    task1 = PythonOperator(
        task_id="get_versions",
        python_callable=get_versions,
    )

    task1
