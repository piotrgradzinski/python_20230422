"""
UML class diagram: https://yuml.me/afdfa259.png

Implement the Basket class that allows adding products in a certain number to a shopping cart.
Implement a method that calculates the total value of the shopping cart and prints information
about the contents of the cart.
Implement a method that calculates how many products are in the shopping cart.
Implement a property indicating whether the shopping cart is empty.
Adding the same product to the cart twice should create only one item.

Usage example:
water = Product(1, 'Water', 10.00)
ice_cream = Product(2, 'Ice cream', 5.00)

basket = Basket()
basket.add_product(water, 5)
basket.add_product(ice_cream, 2)
basket.count_total_price()  # 60.00
basket.generate_receipt()
'''
Products:
- Water, 10.00 x 5
- Ice cream, 5.00 x 2
Total: 60.00
'''
basket.count_products()  # 2
basket.is_empty()  # False
"""

from ex_1 import Product

class Basket:
    def __init__(self):
        self._items = dict()  # object of class Product as a key, quantity as a value

    def add_product(self, product: Product, quantity: int):
        ...

    def count_total_price(self) -> float:
        ...

    def generate_receipt(self) -> str:
        ...

    def count_products(self) -> int:
        ...

    def is_empty(self) -> bool:
        ...


water = Product(1, 'Water', 10.00)
ice_cream = Product(2, 'Ice cream', 5.00)

basket = Basket()
basket.add_product(water, 5)
basket.add_product(ice_cream, 2)
basket.count_total_price()  # 60.00
receipt = basket.generate_receipt()
print(receipt)
basket.count_products()  # 2
basket.is_empty()  # False
