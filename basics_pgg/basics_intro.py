print("Hello world!")
print('To be or not to be')

# Data types
# string - str
# string is a collection of characters
print('My name is Piotr GG')
print("My name is Piotr GG")

# integer - int
print(10)
print(-1)

# float
print(3.14)
print(3.0)  # this is still a float
print(3.)
print(.5)  # 0.5

print(type(3))  # <class 'int'>
print(type(3.0))  # <class 'float'>

print('3.14')
print(3.14)

print(type('3.14'))  # <class 'str'>
print(type(3.14))  # <class 'float'>

# boolean - bool
# Boolean data type has 2 values: True, False
print(True)
print(False)

# Data type None and has only one value: None
# null, None represent missing or empty value
print(None)

# Operators
print(10 + 3)  # 13
print(10 - 3)  # 7
print(10 * 3)  # 30
print(10 / 3)  # 3.3333333333333335
print(10 // 3)  # 3
print(3.14 * 2.5)

# When I'm using + with 2 strings, I'm connecting those
# two string together, I'm concatenating them
print('My name is ' + 'Piotr GG')

# string * integer
# repeats a 'Hello' string 10 times
print('Hello ' * 10)
print('3.14' * 2)
# print('3.14' / 2)  # will not work: unsupported operand type(s) for /: 'str' and 'int'

# variables
# = assigns value from the right side to the variable on the left side
first_name = 'Piotr'  # this operation is not displaying anything
print(first_name)

first_number = 100
second_number = 50
result = first_number + second_number
print(result)

# print function accepts many argument, so we can display
# several things at once
print(first_number, second_number, result, result * 10)

print('-' * 30)

first_name = 'Piotr'
height = 182

# 1 approach
print('First name:', first_name)  # by default arguments displayed with a print function are separated by space
# First name: Piotr
print('Height:', height)

# 2 approach
print('First name: ' + first_name)
# print('First name: Piotr')
# it's not allowed to concatenate strings with anything else than string
# print('Height: ' + height)  # TypeError: can only concatenate str (not "int") to str
print('Height: ' + str(height))
# print('Height: ' + '182')
# print('Height: 182')

# 3 approach - f-string, formatted string
print(f'First name: {first_name}')
print(f"Height: {height}")

print('-' * 30)

# Python is a weakly typed language
# which means one variable can store different data types
my_variable = 'Piotr'
print(my_variable)

my_variable = 44
print(my_variable)

print('-' * 30)

# Assignment operator
number = 10
print(number)

print('-' * 30)

number = 10
print(number)
number = number + 1
print(number)

number = 10
number = number + 1
print(number)

number = 10
number += 2
print(number)

# +=, -=, *=, /=

print('-' * 30)

# Comparison operators
print(1 == 1)  # True, Warning! We have to = signs, not one!
print(1 != 1)  # False
print(1 > 2)  # False
print(1 < 2)  # True
print(1 <= 1)  # True
print(2 >= 2)  # True

first_number = 10
second_number = 20
print(first_number < second_number)  # True

# modulus operator
print(10 % 3)  # 1
print(10 / 3)  # 3.(3)
print(20 % 6)  # 2

print('-' * 30)

# Logical operators - not, and, or
print(not True)
print(not False)

print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

number = 10
#        True    and         True      -> True
print(number > 5 and number % 2 == 0)  # True

number = 7
#          True  and      False        -> False
print(number > 5 and number % 2 == 0)  # False

print((number > 5 and number % 2 == 0) or number == 7)

print('-' * 30)

number = 88

# if number >= 0 and number <= 100:  # we are checking if the number is in range
if 0 <= number <= 100:
    print('Number is in a range 0-100')
    if number < 50:
        print('Number is in a range 0-50')
    else:
        print('Number is in a range 50-100')
elif 101 <= number <= 200:  # elif number >= 101 and number <= 200:
    print('Number in a range 101-200')
else:
    print('Number is out of range.')
