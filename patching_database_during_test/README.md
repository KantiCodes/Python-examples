### Description:
This example shows the difference in two ways of patching the concrete database connection when testing business logic of some module using the database operations. The main point of intrest is
under [tests/test_module](https://github.com/KantiCodes/Python-examples/blob/main/patching_database_during_test/tests/module_test.py) the test for **moduleA** passes while the **moduleB** fails to patch and rasies **NotImplementedError**

* [database.py](https://github.com/KantiCodes/Python-examples/blob/main/patching_database_during_test/database.py) - business logic and method for connecting to concrete database (which currently rasies **NotImplementedError**)
* [moduleA.py](https://github.com/KantiCodes/Python-examples/blob/main/patching_database_during_test/moduleA.py) and [moduleB.py](https://github.com/KantiCodes/Python-examples/blob/main/patching_database_during_test/moduleB.py) - some modules using the database to add a new person to the database
* [tests/conftest.py](https://github.com/KantiCodes/Python-examples/blob/main/patching_database_during_test/tests/conftest.py) - file with 2 fixture to accordingly patching driver for **moduleA** and **moduleB**
