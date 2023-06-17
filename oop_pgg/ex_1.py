"""
Implement a Product class that stores information about the price, name and ID of the product.
Implement a method that prints the product information to the console and returns a description as a string.

Usage example:
> product = Product(1, 'Water', 10.99)
> product.print_info()
Product "Water", id: 1, price: PLN 10.99

Scenario:
1. we create a class
2. we add __init__ (constructor)
3. we add attributes
4. we add print_info(), get_info() methods
5. extra: add type hinting and method documentation
"""

class Product:
    def __init__(self, product_id: int, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price

    def print_info(self):
        print(self.get_info())

    def get_info(self) -> str:
        return f'Product "{self.name}", id: {self.product_id}, price: {self.price} PLN'

    def __str__(self):
        # print('Executing __str__ method')
        return self.get_info()


print(__name__)
# This if statement is safeguard mechanism to avoid code execution when importing this file into another file
# __name__ is a special variable that "stores the name of the file"
# if I'm executing ex_1.py __name__ == '__main__'
# if I will import ex_1 within product_import_test, __name__ == 'ex_1'
if __name__ == '__main__':
    water = Product(1, 'Water', 10.99)
    water.print_info()
    print(water)

    info = water.get_info()
    info = info.upper()
    print(info)

    # instead of writing those two lines
    # I want to give the developer possibility to print it.
    info = water.get_info()
    print(info)

    # __str__ method is executed by Python
    # when we are trying to convert our object into string
    converted = str(water)

