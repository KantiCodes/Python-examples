# This will not be patched during tests
# from testing_examples.database import get_driver

# Get driver be patched by confest during tests
from testing_examples import database


def main():
    kelly = {"name": "Kelly", "happy": True}
    driver = database.get_driver()
    driver.add_person(kelly)
