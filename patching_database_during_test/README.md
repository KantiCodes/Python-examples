### Description:
This example shows the difference in two ways of patching the concrete database connection when testing a module that uses the database.

- **good** has been correctly patched and ```get_driver``` method is replacted during the test
- **bad** on the other has been patched incorrectly and attempts to use actual ```get_driver``` method during the test(which currently raises NotImplementError)


_See https://docs.python.org/3/library/unittest.mock.html#where-to-patch for more info on where to patch_

The difference between **good.py** and **bad.py** is in the way they import ```get_driver``` method from **database.py**, one imports the entire object while the other imports just the method


* [database.py](https://github.com/KantiCodes/Python-examples/blob/main/patching_database_during_test/database.py) - business logic and method for connecting to concrete database (which currently rasies **NotImplementedError**)
* [good.py](https://github.com/KantiCodes/Python-examples/blob/main/patching_database_during_test/good.py) and [bad.py](https://github.com/KantiCodes/Python-examples/blob/main/patching_database_during_test/bad.py) - some modules using the database to add a new person to the database
* [tests/conftest.py](https://github.com/KantiCodes/Python-examples/blob/main/patching_database_during_test/tests/conftest.py) - file with 2 fixture to accordingly patching driver for **good** and **bad**
* [tests/test_module](https://github.com/KantiCodes/Python-examples/blob/main/patching_database_during_test/tests/module_test.py) - file with the 2 tests 
