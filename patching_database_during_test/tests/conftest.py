import pytest


@pytest.fixture(name="db_driver_a", autouse=False)
def db_driver1(mocker):
    """Patch using method patching"""
    from patching_database_during_test.database import DBDriver

    driver = DBDriver([])
    mocker.patch("patching_database_during_test.database.get_driver", return_value=driver)
    yield driver
