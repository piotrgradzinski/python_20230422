"""
Write a program listing all numbers from 0 to 100 that are divisible by 3 or by 5.
Also write how many such numbers occurred in this interval.

Numbers divisible by 3 or 5:
0
3
5
...
96
99
100

In the range 0-100 there are 48 numbers divisible by 3 or 5

Hint: how to check if number is divisible by 2?
number % 2 == 0
"""

how_many = 0
for number in range(0, 101):
    if number % 3 == 0 or number % 5 == 0:
        print(number)
        how_many += 1

print()  # just for having an empty line
print(f"In the range 0-100 there are {how_many} numbers divisible by 3 or 5")
