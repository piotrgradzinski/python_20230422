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
