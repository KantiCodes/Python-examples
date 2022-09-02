# This will be patched during tests
# Get driver be patched by confest during tests
from patching_database_during_test import database


def main():
    kelly = {"name": "Kelly", "happy": True}
    driver = database.get_driver()
    driver.add_person(kelly)
