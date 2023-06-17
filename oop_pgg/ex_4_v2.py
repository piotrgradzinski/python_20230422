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
from collections import defaultdict

import pytest

from ex_1 import Product


class Basket:
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


water = Product(1, 'Water', 10.00)
ice_cream = Product(2, 'Ice cream', 5.00)

basket = Basket()
print(basket.is_empty)  # True
basket.add_product(water, 5)
basket.add_product(ice_cream, 2)

print(basket.count_total_price())  # 60.00
receipt = basket.generate_receipt()
print(receipt)
print(basket.count_products())  # 2
print(basket.is_empty)  # False

# _items in Basket class
# print(basket._items.keys())  # Access to a protected member _items of a class

# __items in Basket class
# print(basket.__items.keys())  # AttributeError: 'Basket' object has no attribute '__items'
# print(basket._Basket__items.keys())  # it's possible but we shouldn't do that

def test_basket_is_empty_after_creation():
    b = Basket()
    assert b.is_empty is True

def test_basket_is_not_empty_after_adding_product():
    b = Basket()
    p1 = Product(1, 'Water', 5.0)
    b.add_product(p1, 5)
    assert b.count_products() == 1
    assert b.is_empty is False

def test_adding_product_two_times():
    b = Basket()
    p1 = Product(1, 'Water', 5.0)
    b.add_product(p1, 1)
    b.add_product(p1, 2)
    assert b.count_products() == 1
    assert b.count_total_price() == 15


def test_adding_two_product_and_price_check():
    b = Basket()
    p1 = Product(1, 'Water', 5.0)
    p2 = Product(2, 'Chocolate', 10.0)
    b.add_product(p1, 10)
    b.add_product(p2, 2)
    assert b.count_total_price() == 70.0


def test_adding_not_product():
    b = Basket()
    with pytest.raises(TypeError):
        b.add_product('string, not a product', 2)

def test_adding_negative_quantity_of_product():
    b = Basket()
    p1 = Product(1, 'Water', 5.0)
    with pytest.raises(ValueError):
        b.add_product(p1, -5)
