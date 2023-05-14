"""
Create the following data structures using comprehension expressions:
- (a) a list containing floating point numbers from 0.0 to 1.0 with increments of 0.1
Use range from 0 to 11 and divide the number by 10.
[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

- (b) a set of tuples containing 3 elements each - a given number, its square and its cube - in the range from -10 to 10
{(-8, 64, -512), (-1, 1, -1), (9, 81, 729), (4, 16, 64), (5, 25, 125), (2, 4, 8), (-9, 81, -729), (3, 9, 27), (-6, 36, -216), (7, 49, 343), (-4, 16, -64), (0, 0, 0), (-7, 49, -343), (10, 100, 1000), (-5, 25, -125), (-2, 4, -8), (8, 64, 512), (-10, 100, -1000), (-3, 9, -27), (6, 36, 216), (1, 1, 1)}

- (c) a dictionary created from set of strings that maps strings to their length
{
    'a': 1,
    'Tom': 3,
    'Amy': 3,
    'To be or not to be': 18
}
"""

a = [number / 10 for number in range(0, 11)]
print(a)

a = []
for number in range(0, 11):
    a.append(number / 10)
print(a)


b = {(number, number ** 2, number ** 3) for number in range(-10, 11)}
print(b)

b = set()
for number in range(-10, 11):
    tmp_tuple = (number, number ** 2, number ** 3)
    b.add(tmp_tuple)
    # b.add((number, number ** 2, number ** 3))
print(b)


strings = {'a', 'Amy', 'Tom', 'To be or not to be'}
c = {string: len(string) for string in strings}
print(c)

c = dict()
for string in strings:
    c[string] = len(string)
print(c)
