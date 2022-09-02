import math
import pytest
import module


def test_get_sin_PATCHED_WITH_cos(mocker):
    """
    In this test we will patch the math.sin function with math.cos and
    then invoke it indirectly from our module
    
    sin(0) = 0
    cos(0) = 1

    Hence we expect the result of get_sin(0) to be 1
    """

    mocked_add = mocker.patch("math.sin", side_effect=math.cos)  # Patch math.sin with math.cos
    res = module.get_sin(0)
    mocked_add.assert_called_once_with(0)
    assert res == 1


def test_get_user_WHEN_user_MISSING(mocker):
    missing_user_id = "user_id_not_present_in_database"
    expected_call = f"https://api.github.com/user/{missing_user_id}"
    patched_call = mocker.patch(
        "ghapi.core.GhApi.__call__", return_value={"commits": 10, "prs": 0}
    )
    user = module.get_user(missing_user_id)

    patched_call.assert_called_once_with(expected_call)
    assert user["commits"] == 10
    assert user["prs"] == 0
