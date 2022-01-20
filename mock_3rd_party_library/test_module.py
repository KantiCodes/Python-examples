import math
import pytest
import module


def test_get_sin_PATCHED_WITH_cos(mocker):
    mocked_add = mocker.patch("math.sin", side_effect=math.cos)
    res = module.get_sin(0)
    mocked_add.assert_called_once_with(0)
    assert res == 1


def test_get_user_WHEN_user_MISSING(mocker):
    missing_user_id = "user_id_not_present_in_database"
    patched_api_call = mocker.patch(
        "ghapi.core.GhApi.__call__", return_value={"commits": 10, "prs": 0}
    )
    user = module.get_user(missing_user_id)
    print(user)
    assert user["commits"] == 10
