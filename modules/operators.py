def start_task():
    return """
\tstart_task = DummyOperator(task_id="start")
"""
    
def stop_task():
    return """
\tstop_task = DummyOperator(task_id="stop")
"""
    
def bash_operator_echo(index):
    return """
\ttask_{index} = BashOperator(task_id='task_{index}', bash_command="echo 'command executed from BashOperator'")
""".format(index=index)

def bash_operator_sleep(index, sleep_time_in_sec):
    return """
\ttask_{index} = BashOperator(task_id='task_{index}', bash_command="sleep {sleep_time}s")
""".format(index=index,sleep_time=sleep_time_in_sec)

def python_operator_task_sleep(index, sleep_time_in_sec):
    return """
\ttask_{index} = PythonOperator(
\ttask_id='task_{index}',
\tpython_callable=lambda: time.sleep({sleep_time}),
\t)
""".format(index=index,sleep_time=sleep_time_in_sec)

def python_operator_task_print(index):
    return """
\ttask_{index} = PythonOperator(
\ttask_id='task_{index}',
\tpython_callable=lambda: print('Hello from Python operator'))
""".format(index=index)