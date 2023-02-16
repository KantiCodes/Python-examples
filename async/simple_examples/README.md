# Description
Simple example of running functions conqurently using asyncio.task, although each function waits for 2 seconds, the code finishes after about 2 seconds


# Usage 
## Execute a valid command without exception propagating
```python3.10 async/simple_examples/run_asyncio_task.py```

Outputs:
```
started at 08:22:05.918307
Task1
Task2
Task3
Task4
Finished at 08:22:07.919902
Worked for ~ 2.001595 seconds
```

