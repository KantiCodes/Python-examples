# This will not be patched during tests as we are importing 
from patching_database_during_test.database import get_driver

def main():
    kelly = {"name": "Kelly", "happy": True}
    driver = get_driver()  # Raises not implemented error
    driver.add_person(kelly)
