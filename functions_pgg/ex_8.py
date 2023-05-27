"""
Implement a function that calculates factorial of a given value.
https://en.wikipedia.org/wiki/Factorial

factorial(5) = 1*2*3*4*5 = 120

Example:
> factorial(5)
120

Version 1
- validate n argument according to the factorial requirements (check wikipedia)
- use for loop with range from 1 to n (included!)
- multiple the consecutive numbers by each other and return the value

Tests
Check several values based on the wikipedia table.
"""
import pytest


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError('n must be non-negative integer')

    result = 1

    for i in range(1, n + 1):
        # result *= i
        result = result * i

    return result


def test_5():
    assert factorial(5) == 120

def test_0():
    assert factorial(0) == 1

def test_valid_values():
    # list of tuples
    # within each tuple (n, result)
    test_data = [(0, 1), (1, 1), (2, 2), (3, 6), (4, 24), (5, 120), (6, 720), (7, 5040), (8, 40320), (9, 362880), (10, 3628800), (11, 39916800), (12, 479001600), (13, 6227020800), (14, 87178291200), (15, 1307674368000), (16, 20922789888000), (17, 355687428096000), (18, 6402373705728000), (19, 121645100408832000), (20, 2432902008176640000),]
    for n, result in test_data:
        assert factorial(n) == result

def test_negative_integer():
    try:
        factorial(-10)
        assert False
    except ValueError:
        assert True

def test_negative_integer2():
    with pytest.raises(ValueError):
        factorial(-10)
