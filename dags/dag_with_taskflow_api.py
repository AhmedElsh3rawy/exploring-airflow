from airflow.sdk import dag, task
from datetime import datetime, timedelta

default_args = {"owner": "ahmed", "retries": 5, "retry_delay": timedelta(minutes=2)}


@dag(
    dag_id="dag_with_taskflow_api",
    default_args=default_args,
    start_date=datetime(2021, 4, 4, 2),
    schedule="@daily",
)
def hello_world_etl():
    @task
    def get_name():
        return "John"

    @task
    def get_age():
        return 20

    @task
    def greet(name, age):
        print(f"Hello, World! My name is {name}", f"and I am {age} years old")

    name = get_name()
    age = get_age()
    greet(name=name, age=age)


greet_dag = hello_world_etl()
