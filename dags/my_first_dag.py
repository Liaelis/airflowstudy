from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator

#não faz nada, mas é utilizado para organizar o fluxo de tarefas no DAG
#O BashOperator, por sua vez, é responsável por executar um script ou comando bash, que executamos no terminal.
#days_ago pega dias anterior define a quantidade de dias
#primeiro parametro nome da dag

with DAG(
    'my_first_dag',
    start_date=days_ago(1),
    schedule_interval='@daily'
) as dag:

        tarefa_1 = EmptyOperator(task_id='tarefa_1')
        tarefa_2 = EmptyOperator(task_id='tarefa_2')
        tarefa_3 = EmptyOperator(task_id='tarefa_3')
        tarefa_4 = BashOperator(
            task_id='cria_pasta',
            bash_command='mkdir -p "home/millenagena/Documents/airflowstudy/pasta" '
        )

        tarefa_1 >> [tarefa_2,tarefa_4]
        tarefa_3 >> [tarefa_4]