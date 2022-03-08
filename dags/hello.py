"""
## The Hello Dag

this dag is an intial test using common operators
my goal here is to just test that my dags can run correctly on 
cloud composer.
"""

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import timedelta

default_args = {
    'owner': 'Jesufemi-o',
    'start_date': airflow.utils.dates.days_ago(0),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'hello_dag',
    default_args=default_args,
    description='liveness monitoring dag',
    schedule_interval="@daily",
    dagrun_timeout=timedelta(minutes=20))

t1 = DummyOperator(task_id='start_workflow', dag=dag, depends_on_past=False)
t2 = BashOperator(
    task_id='echo',
    bash_command='echo test',
    dag=dag,
    depends_on_past=False,
    )

t1 >> t2
