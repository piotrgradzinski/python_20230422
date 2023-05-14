"""
Write a function to check if a given number is a prime number.

Example of use:
is_prime(10)
false
is_prime(17)
true
```
https://en.wikipedia.org/wiki/Prime_number

Prime number is a number which:
- is int
- is bigger than 1
- is not a product of two smaller natural numbers
take all the numbers between 2 and number-1
    check if number is divisible by this number
        return False

Example
NUMBER = 9
for numbers in range(2, 9) take each number from the range as X
    and check if NUMBER is divisible by X. If it is then return False

IF the previous loop finished without returning False, that means,
we didn't find a number with which we can divide our NUMBER, so the NUMBER
is prime, and we can return True.
"""


def is_prime(number):
    ...

