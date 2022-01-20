import math
import pytest
import module


def test_add(mocker):
    mocked_add = mocker.patch("math.sin", side_effect=math.cos)
    res = module.get_sin(0)
    mocked_add.assert_called_once_with(0)
    assert res == 1
