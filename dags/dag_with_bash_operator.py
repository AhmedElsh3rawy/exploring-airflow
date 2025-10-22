from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {"owner": "ahmed", "retries": 5, "retry_delay": timedelta(minutes=2)}

with DAG(
    dag_id="dag_with_bash_operator",
    default_args=default_args,
    description="My first bash operator dag",
    start_date=datetime(2021, 4, 4, 2),
    schedule="@daily",
) as dag:
    task1 = BashOperator(task_id="first_task", bash_command="echo 'I AM TASK ONE!'")

    task2 = BashOperator(task_id="second_task", bash_command="echo 'I AM TASK TWO!!'")

    task3 = BashOperator(task_id="third_task", bash_command="echo 'I AM TASK THREE!!!'")

    task1 >> [task2, task3]
