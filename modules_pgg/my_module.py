"""
modules_pgg/my_module.py

Files / modules should be named according to PEP8.
TL:DR; we can use variable naming approach:
- no spaces
- do not start with number
- do not use dots
"""

def square(number):
    return number ** 2


my_string = 'To be or not to be'
my_numbers = [10, 20, 30, 40, 50]

# Do not execute code in this way when you are creating a module...
# print("Hello from my module...")  # it will be executed when importing this module

"""
to fix this problem, so we can do a trick. 
It's quite popular that one file can be used as module, because we have some useful functions defined there
but in the same time we'd like to be able to run this file and do something. 
when executing this file
__name__ will contain "__main__"
but when imported will become "modules_pgg.my_module"
"""

if __name__ == '__main__':
    # we know that we are running this file and this file is not imported, so we can execute any logic we want
    print("Hello from my module...")
