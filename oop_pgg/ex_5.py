"""
Implement the `Vector` class providing two-dimensional vector functionality.
Vectors should be able to add, subtract, multiply (by number), compare (by length)
and should have a readable string representation.

Example of use:
vector_1 = Vector(x=1, y=2)
vector_2 = Vector(x=1, y=2)
vector_3 = vector_1 + vector_2

Plan:
Magic methods: https://www.python-course.eu/python3_magic_methods.php
1. Which ones we will use?
    __add__, adding two vectors, +, https://www.varsitytutors.com/hotmath/hotmath_help/topics/adding-and-subtracting-vectors
    __sub__, subtracting two vectors, -, https://www.varsitytutors.com/hotmath/hotmath_help/topics/adding-and-subtracting-vectors
    __mul__, multiplying vector by number (not other vector), *,
    __str__, conversion to string
    method len, to calculate vector length (use Pythagorean theorem)
    __eq__, are two vectors equal (in terms of length), ==
    __ne__, are two vectors not equal (in terms of length), !=
    __gt__, is vector a bigger than b (in terms of length), >
    __ge__, is vector a bigger or equal than b (in terms of length), >=
    __lt__, is vector a less than b (in terms of length), <
    __le__, is vector a less than or equal b (in terms of length), <=
2. Check types of the arguments
"""


class Vector:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y


vector_1 = Vector(x=1, y=2)
vector_2 = Vector(x=1, y=2)
