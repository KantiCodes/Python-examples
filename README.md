## Why this repo?
Because I keep solving the same problems over and over and then I endup trying to remember in which project is the solution located :)

## Installing project
Create a virtual environment
* mac/linux ```python3 -m venv .venv```
* windows ```python -m venv .venv```

Activate venv
* mac/linux ```source .venv/bin/activate```
* windows ```.\venv\Scripts\activate```

Install depedencies (on activated venv)
* Either ```python -m pip install -r requirements.in```
* Or ```python -m pip install -r requirements.txt```

## Examples

### Patching_database_during_test
Example of a fixture that you insert into ```conftest.py``` that allows you to patch the database used by SUT for a different - test one.

### Bare_raise_exception
This examples targets command lines tools and shows how to enable a flag for verbose output of the error in the tool
