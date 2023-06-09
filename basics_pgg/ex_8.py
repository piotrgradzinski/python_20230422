"""
Write a program that calculates the square of the first 100 natural numbers
and prints the results to the console.

Sample program output:
1 square equals 1
2 square equals 4
...
10 square equals 100
...
100 square equals 10000
"""

i = 1
while i <= 100:
    print(f'{i} square equals {i * i} {i ** 2}')
    i += 1
