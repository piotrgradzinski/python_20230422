"""
Create a function that will return the n-th value of the Fibonacci sequence.
https://en.wikipedia.org/wiki/Fibonacci_sequence
https://medium.com/launch-school/recursive-fibonnaci-method-explained-d82215c5498e

Fibonacci sequence
fib(0) = 0
fib(1) = 1
fib(n) = fib(n-1) + fib(n-2)
"""
import pytest


def fib(n: int) -> int:
    if n < 0:
        raise ValueError('n must be non-negative')

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def test_0():
    assert fib(0) == 0

def test_1():
    assert fib(1) == 1

def test_10():
    assert fib(10) == 55

def test_negative():
    with pytest.raises(ValueError):
        fib(-10)
