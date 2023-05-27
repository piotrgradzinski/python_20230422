"""
Implement a function that calculates factorial of a given value.
https://en.wikipedia.org/wiki/Factorial

factorial(5) = 1*2*3*4*5 = 120

Example:
> factorial(5)
120

Version 2 - recursion
factorial(5)
5 * factorial(4)
5 * 4 * factorial(3)
5 * 4 * 3 * factorial(2)
5 * 4 * 3 * 2 * factorial(1)
5 * 4 * 3 * 2 * 1 * factorial(0)
5 * 4 * 3 * 2 * 1 * 1

Plan
- check if n equals 0 - if so, return 1
- else, return n multiplied by factorial of n - 1

Recursion
https://en.wikipedia.org/wiki/Recursion_(computer_science)
https://prateekvjoshi.files.wordpress.com/2013/10/part-1.jpg

Recursion
1. Define stop condition
2. Divide more complex task into smaller tasks
3. Execute our function on those smaller tasks
4. Collect results
5. Combine them
6. Return combined result
"""
import pytest


def factorial(n: int) -> int:
    ...


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
