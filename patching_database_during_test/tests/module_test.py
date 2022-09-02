import pytest
from patching_database_during_test import good
from patching_database_during_test import bad
from patching_database_during_test.database import DBDriver

# This passes nicely
def test_module_a(db_driver_a: DBDriver):
    good.main()
    assert db_driver_a.get_person("Kelly")

# This fails with NotImplementedError
def test_module_b(db_driver_a: DBDriver):
    with pytest.raises(NotImplementedError):
        bad.main()
