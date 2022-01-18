from patching_database_during_test.moduleA import main as main_a
from patching_database_during_test.moduleB import main as main_b
from patching_database_during_test.database import DBDriver

# This passes nicely
def test_module_a(db_driver_a: DBDriver):
    main_a()
    assert db_driver_a.get_person("Kelly")

# This fails with NotImplementedError
def test_module_b(db_driver_b: DBDriver):
    main_b()
    assert db_driver_b.get_person("Kelly")
