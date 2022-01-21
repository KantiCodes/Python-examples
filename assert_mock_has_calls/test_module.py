from unittest.mock import call
import datetime


def test_make_dates(mocker):
    # Prepare some sequences to be turned into dates
    tuple_dates = [
        (1998, 12, 20),  # Me!
        (1998, 1, 3),
        (1998, 4, 10),
    ]

    # Mock
    mocked_date = mocker.patch("datetime.date")

    # Call the function for each date
    for tuple_date in tuple_dates:
        datetime.date(*tuple_date)

    # Expected calls - first element of calls will be call(1998, 12, 20)
    calls = [call(*d) for d in tuple_dates]

    # If we want to compare the calls in any order we can do the following
    mocked_date.assert_has_calls(calls, any_order=True)

    # We can also check if the two lists are the same
    assert calls == mocked_date.mock_calls
