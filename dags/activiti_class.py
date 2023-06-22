from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator

with DAG(
    'activity_class',
    start_date=days_ago(1),
    schedule_interval='@daily'
)as dag:
        def cumprimentos():
                print("Boas-vindas ao Airflow!")
        tarefa1 = PythonOperator(
                task_id='cumprimentos',
                python_callable=cumprimentos
        )


