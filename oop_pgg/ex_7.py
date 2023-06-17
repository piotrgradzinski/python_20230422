"""
Implement a class method that creates a basket based on the provided list of products.
Each of them should be added to the basket only once.

Example of use:
prod_1 = Product(1, 'Water', 1.99)
prod_2 = Product(2, 'Crisps', 5.99)

# with class method
basket = Basket.with_products([prod_1, prod_2])  # list of Product objects

# without class method
basket = Basket()
basket.add_product(prod_1, 1)
basket.add_product(prod_2, 2)

How to do it?
- create with_products class method
    - create a new Basket object
    - iterate through a list with products (instances of Product class)
    - invoke .add_product on newly created basket and add product
"""
from collections import defaultdict
from typing import List

from oop_pgg.ex_1 import Product


class Basket:
    @classmethod
    def with_products(cls, products: List[Product]):
        ...

    def __init__(self):
        self.__items = defaultdict(int)

    def add_product(self, product: Product, quantity: int):
        if quantity <= 0:  # business decision whether quantity can be negative
            raise ValueError('Quantity must be positive.')

        if not isinstance(product, Product):
            raise TypeError('You can only add Product to this basket.')

        self.__items[product] += quantity

    def count_total_price(self) -> float:
        return sum([product.price * quantity for product, quantity in self.__items.items()])

    def generate_receipt(self) -> str:
        receipt = ['Products']
        for product, quantity in self.__items.items():
            receipt.append(f'- {product.name}, {product.price} x {quantity}')
        receipt.append(f'Total: {self.count_total_price()}')
        return '\n'.join(receipt)

    def count_products(self) -> int:
        return len(self.__items)

    @property
    def is_empty(self) -> bool:
        return not self.__items  # leveraging empty/non-empty dict to bool conversion


prod_1 = Product(1, 'Water', 1.99)
prod_2 = Product(2, 'Crisps', 5.99)

basket = Basket.with_products([prod_1, prod_2])
print(basket.count_products())
