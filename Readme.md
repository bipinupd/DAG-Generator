## Generating random DAGs to test airflow environment

The python program generates DAGs based on the configuration.

Example of the configuration:

```
{
    "number_of_dags_to_generate": 30,
    "file_start_index": 1,
    "min_number_of_task_in_dag": 10,
    "max_number_of_task_in_dag": 30,
    "percentage_of_job_in_parallel": 20,
    "number_of_operators_defined": 4,
    "task_min_time_is_sec":  15,
    "task_max_time_in_sec": 50,
    "schedules": ["min", "hour", "day", "everyhalfhour", "everyhour"]
}
```

- number_of_dags_to_generate: Number of DAG you want to generate
- file_start_index: Start of the index number for the DAG file.
- min_number_of_task_in_dag: Miniumum number of task in a generated DAG
- max_number_of_task_in_dag: Maximum number of tasks in a generated DAG
- percentage_of_job_in_parallel: Percentage of tasks in a DAG that runs in parallel
- number_of_operators_defined: Number of operator defined in operators.py. Current we have 4 coperators (bash and python)
- task_min_time_is_sec: Minimum time used by Bash and Python sleep operators
- task_max_time_in_sec: Maximum time used by Bash and Python sleep operators
- schedules: Defined when the DAGs are schedules. `min` picks ramdom min when the DAG is scheduled, `hour` picks random min (0-59) and randon hours (0-23) when DAG is scheduled. `day` (default) picks the random min, random hour and random day.


Run the following command, the generated DAGs will be in `out/` folder
``` python3 main.py```