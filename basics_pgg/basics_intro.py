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
