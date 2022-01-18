# This will not be patched during tests
from testing_examples.database import get_driver

# Get driver be patched by confest during tests
# from testing_examples import database


def main():
    kelly = {"name": "Kelly", "happy": True}
    driver = get_driver()  # Raises not implemented error
    driver.add_person(kelly)
