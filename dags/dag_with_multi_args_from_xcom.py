from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {"owner": "ahmed", "retries": 5, "retry_delay": timedelta(minutes=2)}


def greet(age, ti):
    fname = ti.xcom_pull(task_ids="get_name", key="first_name")
    lname = ti.xcom_pull(task_ids="get_name", key="last_name")
    print(f"Hello, World! My name is {fname} {lname}", f"and I am {age} years old")


def get_name(ti):
    ti.xcom_push(key="first_name", value="John")
    ti.xcom_push(key="last_name", value="Foster")


with DAG(
    dag_id="dag_with_args_from_xcom2",
    default_args=default_args,
    start_date=datetime(2021, 4, 4, 2),
    schedule="@daily",
) as dag:
    task1 = PythonOperator(
        task_id="greet",
        python_callable=greet,
        op_kwargs={"age": 20},  # this pass agrs to greet
    )

    task2 = PythonOperator(task_id="get_name", python_callable=get_name)

    task2 >> task1
