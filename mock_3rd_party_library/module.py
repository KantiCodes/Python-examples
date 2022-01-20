import math
from ghapi.core import GhApi
from urllib.error import HTTPError


api = GhApi(owner="Bartek")


def get_sin(a):
    return math.sin(a)


def get_user(user_id):
    """Returns the user from the database or uses github to get the data"""
    database = {
        "userid111": {"commits": 50, "prs": 1},
        "userid222": {"commits": 1000, "prs": 30},
    }
    user = database.get(user_id)
    if user is None:
        user = get_user_by_id(user_id)
    return user


def get_user_by_id(user_id):
    try:
        return api.__call__(f"https://api.github.com/user/{user_id}")
    except HTTPError:
        return None
