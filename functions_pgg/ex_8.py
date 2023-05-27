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


def factorial(n: int) -> int:
    result = 1

    for i in range(1, n + 1):
        # result *= i
        result = result * i

    return result


def test_5():
    assert factorial(5) == 120

def test_0():
    assert factorial(0) == 1




