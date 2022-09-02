import math
from ghapi.core import GhApi
from urllib.error import HTTPError

DATABASE = {
    "userid111": {"commits": 50, "prs": 1},
    "userid222": {"commits": 1000, "prs": 30},
}

api = GhApi(owner="Bartek")


def get_sin(a):
    return math.sin(a)


def get_user(user_id):
    """
    Attempts to get the user information from the database.
    If the user is not present in the database then it will attempt to fetch it from Github
    """

    user = DATABASE.get(user_id)
    if user is None:
        user = get_user_by_id(user_id)
    return user


def get_user_by_id(user_id):
    return api.__call__(f"https://api.github.com/user/{user_id}")

