from time import sleep
import json
import random
import modules.initDag
import modules.operators
import math

def getConfig():
    f = open ('config.json', "r")
    data = json.loads(f.read())
    f.close()
    return data

# header for all dags
def getInitContent(i):
    modules.initDag.getInitDag(i)

# task for all dags
def getTaskDag(min_number_of_task_in_dag):
    print(min_number_of_task_in_dag)
    file = open("modules/python-operator.py")
    data = file.read()
    file.close()
    return data

# TODO - use all config variables, and add nuew variable to config: schedule_interval 
def main():
    # read config file
    data = getConfig()
    
    number_of_dags_to_generate = data['number_of_dags_to_generate']
    min_number_of_task_in_dag = data['min_number_of_task_in_dag']
    max_number_of_task_in_dag = data['max_number_of_task_in_dag']
    task_min_time_is_sec = data['task_min_time_is_sec']
    task_max_time_in_sec = data['task_max_time_in_sec']
    percentage_of_job_in_parallel = data['percentage_of_job_in_parallel']
    number_of_operators_defined = data['number_of_operators_defined']
    file_index = data['file_start_index']
    schedules = data['schedules']
    # creatting DAG's files
    for i in range(number_of_dags_to_generate):
        task_list = []
        dagf = open(f"out/dagFile_{file_index + i}.py","w+")
        dagf.write(modules.initDag.getInitDag(file_index + i,schedules[random.randrange(0,len(schedules)-1)]))
        dagf.write(modules.operators.start_task())
        dagf.write(modules.operators.stop_task())
        for task_index in range(random.randrange(min_number_of_task_in_dag,max_number_of_task_in_dag)):
            task_list.append("task_{index}".format(index=task_index))
            if (task_index % number_of_operators_defined == 0):
                dagf.write(modules.operators.bash_operator_echo(task_index))
            elif (task_index % number_of_operators_defined == 1):
                dagf.write(modules.operators.bash_operator_sleep(task_index, random.randrange(task_min_time_is_sec, task_max_time_in_sec)))
            elif (task_index % number_of_operators_defined == 2):
                dagf.write(modules.operators.python_operator_task_sleep(task_index, random.randrange(task_min_time_is_sec, task_max_time_in_sec)))
            else:
                dagf.write(modules.operators.python_operator_task_print(task_index))
        no_tasks_in_parallel = math.ceil(percentage_of_job_in_parallel/100 * len(task_list))
        parallel_tasks = []
        if (no_tasks_in_parallel>1):
            for parallel_task_index in range(no_tasks_in_parallel):
                parallel_tasks.append(task_list.pop())
            task_list.insert(random.randrange(1,len(task_list)-2),"[{task}]".format(task=",".join(parallel_tasks)))
        dagf.write("\n\tchain(start_task,{tasks},stop_task)".format(tasks=",".join(task_list)));  
        dagf.close()
    

if __name__ == "__main__":
    main()

