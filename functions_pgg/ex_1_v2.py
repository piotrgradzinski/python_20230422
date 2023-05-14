"""
Create a simple, function based calculator
1. Ask for 2 numbers
2. Ask for operation: (+, -, *, /)
3. Do the calculation and present results
"""


def addition(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 / number_2

def get_users_input():
    users_number_1 = float(input('Provide number 1: '))
    users_number_2 = float(input('Provide number 2: '))
    operation = input('Provide operation (+, -, *, /): ')
    return (users_number_1, users_number_2, operation)  # returning a tuple

def calculate(users_number_1, users_number_2, operation):
    if operation == '+':
        result = addition(users_number_1, users_number_2)
    elif operation == '-':
        result = subtract(users_number_1, users_number_2)
    elif operation == '*':
        result = multiply(users_number_1, users_number_2)
    elif operation == '/':
        result = divide(users_number_1, users_number_2)
    else:
        result = None

    if result is not None:
        print(f'{users_number_1} {operation} {users_number_2} = {result}')
    else:
        print('Unknown operation! Try again!')


users_input = get_users_input()
calculate(users_input[0], users_input[1], users_input[2])
