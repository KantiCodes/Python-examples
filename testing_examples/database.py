from typing import List
from typing import Union

# some database code


class DBDriver:
    """Business layer for database connection"""

    def __init__(self, database: List[dict]) -> None:
        self.__database = database

    def change_moods(self):
        for person in self.__database:
            person["happy"] = not person["happy"]

    def add_person(self, person: dict):
        self.__database.append(person)

    def get_person(self, name: str) -> Union[dict, None]:
        for person in self.__database:
            if person["name"] == name:
                return person

    def get_all(self):
        return self.__database


def __get_production_database():
    "Concrete database connection to prod DB"
    prod_db = [
        {"name": "Pam", "happy": False},
        {"name": "Creed", "happy": True},
        {"name": "Jimmothy", "happy": False},
    ]
    return DBDriver(database=prod_db)


def get_driver() -> DBDriver:
    raise NotImplementedError
