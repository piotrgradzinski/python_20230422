"""

"""


class Person:
    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self):
        print(f'Hello! My name is {self.first_name} {self.last_name}!')

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


person_piotr = Person('Piotr', 'GG')
print(str(person_piotr))
print(person_piotr)
print(person_piotr.first_name)
print(person_piotr.last_name)
person_piotr.say_hello()

person_john = Person()
person_john.first_name = 'John'
print(person_john)
print(person_john.first_name)
person_john.say_hello()

person_mary = Person()
person_mary.last_name = 'Doe'
print(person_mary)
print(person_mary.first_name)
print(person_mary.last_name)
person_mary.say_hello()

print('-' * 30)

"""
Special methods, magic methods, dunder method (dunder - double underscore)
https://piotr.gg/python/python3-dunder-methods-summary.html
"""

class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f'I am a Number and my value is {self.value}'

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
        else:
            return Number(self.value + other)


n1 = Number(10)
n2 = Number(20)

# without __str__: <__main__.Number object at 0x100c0eed0>
# with __str__: I am a number and my value is 10
print(str(n1))
print(str(n2))

n3 = n1 + n2  # n1.__add__(n2)
print(n3)

n3 = n1.__add__(n2)
print(n3)

n4 = n1 + 10  # Number + int
print(n4)

n5 = n1 + 10.5  # Number + float
print(n5)
