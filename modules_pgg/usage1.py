"""
modules_pgg/usage1.py

We will be using the content of my_module in this file.
"""

import modules_pgg.my_module

print(modules_pgg.my_module.my_string)
print(modules_pgg.my_module.my_numbers)
print(modules_pgg.my_module.square(4))
print(modules_pgg.my_module.__file__)  # full path to the file on disc

import pytest
print(pytest.__file__)

