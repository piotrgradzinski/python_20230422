"""
Write a program that counts the number of unique numbers entered by the user.
Check how many of these numbers are even numbers in the range 0-100 -
to do this use the intersection operator.

We have to solve 2 problems:
1 - how many unique elements user provided?
    in while loop get the data from the user to set, "end" string breaks the loop
    after the loop we show how many unique numbers were provided (the length of the set)
    and the numbers itself

2 - how many even numbers were provided in the range from 0 to 100
create a set with even numbers - use for loop and range(0, 101, 2) function
use a set intersection to show which elements provided by the user met criteria
"""

numbers = set()

while True:
    number = input('Provide a number: ')
    if number == 'end':
        break
    else:
        numbers.add(int(number))

print(f"Number of unique numbers: {len(numbers)}")

even_numbers = set()
for number in range(0, 101, 2):
    even_numbers.add(number)

print(f"Number of even, unique numbers between 0-100: {len(numbers.intersection(even_numbers))}")
