import pytest


@pytest.fixture(name="db_driver_a", autouse=False)
def db_driver1(mocker):
    """Patch using method patching"""
    from testing_examples.database import DBDriver

    driver = DBDriver([])
    mocker.patch("testing_examples.database.get_driver", return_value=driver)
    yield driver


@pytest.fixture(name="db_driver_b", autouse=False)
def db_driver2(mocker):
    """Patch using object patching"""
    from testing_examples import database

    driver = database.DBDriver([])
    mocker.patch.object(database, "get_driver", return_value=driver)
    yield driver
