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
        print(self.get_into())

    def get_into(self) -> str:
        return f'Product "{self.name}", id: {self.product_id}, price: {self.price} PLN'


water = Product(1, 'Water', 10.99)
water.print_info()
