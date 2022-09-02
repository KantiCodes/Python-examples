# Why this repo?
Because I keep solving the same problems over and over and then I endup trying to remember in which project is the solution located :)

# Installation & usage
Ran on **python 3.9.13** but any python3 should do.

First you need ```cd``` to the example that yo want to execute 

Create a virtual environment
* mac/linux ```python3 -m venv .venv```
* windows ```python -m venv .venv```

Activate venv
* mac/linux ```source .venv/bin/activate```
* windows ```.\venv\Scripts\activate```

Install depedencies (on activated venv)
* Either ```python -m pip install -r requirements.in```
* Or ```python -m pip install -r requirements.txt``` if I did put those in :D



# Examples

## [assert_mock_has_calls](https://github.com/KantiCodes/Python-examples/blob/main/assert_mock_has_calls)
Given a mocked object assert that it has many calls (in any order)

## [bare_raise_exception](https://github.com/KantiCodes/Python-examples/blob/main/bare_raise_exception)
This examples targets command lines tools and shows how to enable a flag for verbose output of the error in the tool

## [patch_modules](https://github.com/KantiCodes/Python-examples/blob/main/patch_modules)
Simple patching of modules during test

## [patch_with_iterable](https://github.com/KantiCodes/Python-examples/blob/main/patch_with_iterable)
When the same method is supposed to return different things, one can patch it with iterable and allow each call to return something else

## [patching_database_during_test](https://github.com/KantiCodes/Python-examples/blob/main/patching_database_during_test)
Example of a fixture that you insert into ```conftest.py``` that allows you to patch the database used by SUT for a different - test one.

