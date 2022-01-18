### Description:
This example shows the difference in two ways of patching the concrete database connection when testing a module that uses the database.

- **moduleA** has been correctly patched and ```get_driver``` method is replacted during the test
- **moduleB** on the other has been patched incorrectly and attempts to use actual ```get_driver``` method during the test(which currently raises NotImplementError)

The difference between **moduleA.py** and **moduleB.py** is in the way they import ```get_driver``` method from **database.py**, one imports the entire object while the other imports just the method


* [database.py](https://github.com/KantiCodes/Python-examples/blob/main/patching_database_during_test/database.py) - business logic and method for connecting to concrete database (which currently rasies **NotImplementedError**)
* [moduleA.py](https://github.com/KantiCodes/Python-examples/blob/main/patching_database_during_test/moduleA.py) and [moduleB.py](https://github.com/KantiCodes/Python-examples/blob/main/patching_database_during_test/moduleB.py) - some modules using the database to add a new person to the database
* [tests/conftest.py](https://github.com/KantiCodes/Python-examples/blob/main/patching_database_during_test/tests/conftest.py) - file with 2 fixture to accordingly patching driver for **moduleA** and **moduleB**
* [tests/test_module](https://github.com/KantiCodes/Python-examples/blob/main/patching_database_during_test/tests/module_test.py) - file with the 2 tests 
