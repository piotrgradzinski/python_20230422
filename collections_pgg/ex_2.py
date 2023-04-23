"""
Write a program that calculates the average of numbers provided by the user.
To store the numbers use list. Allow up to 10 numbers to be entered.
Use the `len()`, `sum()` built-in function.
"""

numbers = []

while len(numbers) < 10:
    user_number = float(input('Provide a number: '))
    numbers.append(user_number)

average = sum(numbers) / len(numbers)

print(f'The average of provided numbers is {average:.2f}')
