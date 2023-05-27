"""
modules_pgg/usage3.py

it's not a best practise...
The best practise is to place imports on top of the file.
"""
my_string = 'Hello Guys!'
print(my_string)

# this step overwrites my_string variable created in line 7
from modules_pgg.my_module import my_string

print(my_string)
