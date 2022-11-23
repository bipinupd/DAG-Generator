import datetime
import random
def getInitDag(dag_number, schedule):
    today=datetime.datetime.now()
    if (schedule == "min"):
        dag_schedule="{min} * * * *".format(min=random.randrange(0,59))
    elif (schedule == "hour"):
         dag_schedule="{min} {hour} * * *".format(min=random.randrange(0,59), hour=random.randrange(0,23))
    elif (schedule == "everyhalfhour"):
         dag_schedule="*/30 * * * *"
    elif (schedule == "everyhour"):
         dag_schedule="0 * * * *"
    else:
        dag_schedule="{min} {hour} {day} * *".format(min=random.randrange(0,59), hour=random.randrange(0,23), day=random.randrange(1,28))
        
    lines = """import time
from datetime import datetime
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.models.baseoperator import chain

default_args = {{
    'owner': 'Airflow',
    'start_date': datetime({start_year}, {start_month}, {start_day}),
}}

with DAG(
    dag_id='test_dag_{dag_id}',
    schedule_interval='{schedule}',
    default_args=default_args,
    catchup=False
) as dag:
    """.format(dag_id=dag_number,start_year=today.year,
               schedule=dag_schedule,start_month=today.month,start_day=today.day)
    return lines

