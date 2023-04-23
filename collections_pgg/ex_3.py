"""
Write a program that counts occurrences of positive
and negative numbers in a given list of integers.

https://en.wikipedia.org/wiki/0#Mathematics
"0 is neither positive nor negative"
"""

numbers = [1, 2, 3, -100, -10, 0, 4]

positive = 0
negative = 0

for number in numbers:
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1

print(f'Positive: {positive}, negative: {negative}')
