"""
Create a function that will calculate an average value from its arguments.
Leverage *args mechanism for that.
Function invoked without arguments should return None

ex. average(10, 20, 30) -> 20
"""


def average(*numbers):
    if len(numbers) == 0:
        return None

    return sum(numbers) / len(numbers)


def test_no_numbers():
    assert average() is None


def test_several_numbers():
    assert average(10, 20, 30) == 20
