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

print('-' * 30)

"""
Inheritance
"""


# http://yuml.me/preview/ae3a32a3
class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self):
        print(f"Hello! My name is {self.first_name} {self.last_name}")

    def __str__(self):
        return f"Person<{self.first_name}, {self.last_name}>"

class Student(Person):
    def __init__(self, first_name, last_name, field, year):
        super().__init__(first_name, last_name)  # calls __init__ method from parent object (from Person)
        self.field = field
        self.year = year

    def __str__(self):
        return f"Student<{self.first_name}, {self.last_name}, {self.field}, {self.year}>"


john_doe = Person('John', 'Doe')
print(john_doe)
john_doe.say_hello()

student_anna_doe = Student('Anna', 'Doe', 'security', 2)
print(student_anna_doe)
student_anna_doe.say_hello()

print('-' * 30)

"""
Static methods
So far methods defined in a class accepted `self` as an argument
and thanks to that we were able to execute methods on particular object, instances of the class.

Within a class we can defined static method (using @staticmethod decorator). 
This type of methods are a bit different and they don't accept self argument.
They are consider to be tool methods.
"""


# 1 approach - without static methods
def celsius_to_fahr(celc):
    return celc * 1.8 + 32


def fahr_to_celsius(fahr):
    return (fahr - 32) / 1.8


print(celsius_to_fahr(100))
print(fahr_to_celsius(212))

"""
With the approach 1 we have some issues:
- we have two separate functions that are not related in any way
- they have nothing in common
- it's hard to find any other functions related to temperature conversion

We see that those functions are related to each other, because they convert the temperature
but at the same time they don't share any data between each other. 

To add some context we can group them together within a class and mark them as static methods.
"""

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahr(celc):
        return celc * 1.8 + 32

    @staticmethod
    def fahr_to_celsius(fahr):
        return (fahr - 32) / 1.8


print(TemperatureConverter.celsius_to_fahr(100))
print(TemperatureConverter.fahr_to_celsius(212))



