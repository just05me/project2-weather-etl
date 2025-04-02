from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Импортируем main 
from weather_etl import main

default_args = {
    "owner": "me",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "weather_etl_dag",
    default_args=default_args,
    start_date=datetime(2025, 4, 1),
    # main функция будет запускаться каждые 10 минут
    schedule_interval="*/10 * * * *"  
) as dag:
    run_etl = PythonOperator(
        task_id="run_weather_etl",
        python_callable=main
    )