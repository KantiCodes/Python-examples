import random


def test_iterable_patching(mocker):
    mocker.patch("random.randint", side_effect=[-5, 300, 0])

    first_call = random.randint(10, 100)
    second_call = random.randint(10, 100)
    third_call = random.randint(10, 100)
    
    # Will raise an error
    # fourth_call = random.randint(1, 5)

    assert first_call == -5
    assert second_call == 300
    assert third_call == 0
