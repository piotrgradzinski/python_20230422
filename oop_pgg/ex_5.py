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
import math


class Vector:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def __str__(self):  # str(object)
        return f"Vector<x={self._x},y={self._y}>"

    def __add__(self, other):  # vector + vector
        if not isinstance(other, Vector):
            raise TypeError('You can only add Vector')
        return Vector(self._x + other._x, self._y + other._y)

    def __sub__(self, other):  # vector - vector
        if not isinstance(other, Vector):
            raise TypeError('You can only subtract Vector')
        return Vector(self._x - other._x, self._y - other._y)

    def __mul__(self, other):  # vector * number
        if not isinstance(other, int) and not isinstance(other, float):
            raise TypeError('Second operand must be a scalar value: int or float')
        return Vector(self._x * other, self._y * other)

    @property
    def length(self):  # vector.length
        return math.sqrt(self._x ** 2 + self._y ** 2)  # pythagorean theorem

    def __eq__(self, other):  # equal, ==, vector == vector
        if not isinstance(other, Vector):
            raise TypeError('You can compare only Vectors')
        return self.length == other.length


vector_1 = Vector(x=3, y=2)
vector_2 = Vector(x=1, y=3)
print(vector_1)
print(vector_2)
print()

vector_3 = vector_1 + vector_2

print(vector_3)

vector_4 = vector_1 - vector_2
print(vector_4)

vector_5 = vector_1 * 2
print(vector_5)

print(vector_1.length)
print(vector_2.length)

print(vector_1 == vector_2)

vector_6 = Vector(x=1, y=2)
vector_7 = Vector(x=1, y=2)
print(vector_6 == vector_7)

