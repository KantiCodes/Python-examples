# Description
Example of a cli program that asks for a divider and then logs the result of the division


# Usage 
## Execute a valid command without exception propagating
```python app.py 5```

Outputs:
```
Running in silent mode, exceptions will not be shown
divider: 5
result: 0.2
```


## Execute an invalid command without exception propagating
```python app.py 0```

Outputs:
```
Running in silent mode, exceptions will not be shown
divider: 0
```

## Execute an invalid command with exception propagating
```python app.py 0 --verbose```

Outputs
```
divider: 0
Traceback (most recent call last):
  
  ...
  
  File "/Users/bartoszlachowicz/Desktop/CodeProjects/Python-examples/bare_raise_exception/app.py", line 4, in execute
    click.echo(f"result: {1 / divider}")
ZeroDivisionError: division by zero
```

