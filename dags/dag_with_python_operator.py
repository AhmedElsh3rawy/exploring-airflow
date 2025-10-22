from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {"owner": "ahmed", "retries": 5, "retry_delay": timedelta(minutes=2)}


def greet(name, age):
    print(f"Hello, World! My name is {name}", f"and I am {age} years old")


with DAG(
    dag_id="dag_with_python_operator",
    default_args=default_args,
    description="My second airflow dag",
    start_date=datetime(2021, 4, 4, 2),
    schedule="@daily",
) as dag:
    task1 = PythonOperator(
        task_id="greet",
        python_callable=greet,
        op_kwargs={"name": "Ahmed", "age": 20},  # this pass agrs to greet
    )

    task1
