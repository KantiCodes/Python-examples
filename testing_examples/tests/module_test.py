from testing_examples.moduleA import main as main_a
from testing_examples.moduleB import main as main_b
from testing_examples.database import DBDriver


def test_module_a(db_driver_a: DBDriver):
    main_a()
    assert db_driver_a.get_person("Kelly")


def test_module_b(db_driver_b: DBDriver):
    main_b()
    assert db_driver_b.get_person("Kelly")
