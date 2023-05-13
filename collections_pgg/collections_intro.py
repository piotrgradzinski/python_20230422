# Collections
first_name = 'Piotr'

# Tuple
# indexes:  0   1   2   3   4
my_tuple = (10, 20, 30, 40, 50)

print(my_tuple)
# to be able to access elements in tuple we can use indexing operator
print(my_tuple[0])
print(my_tuple[4])

# within a tuple I can mix data types
# indexes   0   1    2              3
my_tuple = (10, 2.5, 'Hello world', True)
print(my_tuple[2])
print(my_tuple[3])
# print(my_tuple[10])  # IndexError: tuple index out of range

# we can embed collections within other collections

# indexes   0         1                2
my_tuple = ((10, 20), ('a', 'b', 'c'), (True, False))
#            0   1     0    1    2      0     1

print(my_tuple[1])
print(my_tuple[1][2])

print('-' * 30)

# Slicing
# we can fetch a slice of the collection using indexing operator
# my_tuple[start:stop-1:step]
# indexes:  0    1    2    3    4    5    6    7    8    9
my_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
# -indexes: -10  -9   -8   -7   -6   -5   -4   -3   -2   -1

print(my_tuple[0])  #
print(my_tuple[1:3])  # ('b', 'c'); range is left-closed (included), right-open (excluded)
print(my_tuple[1:5])  # ('b', 'c', 'd', 'e')
print(my_tuple[:5])  # ('a', 'b', 'c', 'd', 'e'), assumes 0 as start
print(my_tuple[5:])  # ('f', 'g', 'h', 'i', 'j'), assumes end of the collection
print(my_tuple[:])  # ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print(my_tuple[0:7:2])  # ('a', 'c', 'e', 'g')
print(my_tuple[-1])  # j, last element in the tuple
print(my_tuple[-10:-7])  # ('a', 'b', 'c')
print(my_tuple[:-1])  # ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i') - all elements without the last one
print(my_tuple[5:-2])  # ('f', 'g', 'h')
print(my_tuple[::-1])  # ('j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a')
print(my_tuple[::-2])  # ('j', 'h', 'f', 'd', 'b')
print(my_tuple[5:-6])  # ()
print(my_tuple[6:-7])  # ()
print(my_tuple[-6:5])  # ('e',)
print(my_tuple[3], my_tuple[7])
print(my_tuple[1+3])  # e

# you can't modify the tuple after its creation
# my_tuple[0] = 1000  # TypeError: 'tuple' object does not support item assignment

print(len(my_tuple))  # length of the collection, how many elements we have in a collection
print('a' in my_tuple)  # True, checks if 'a' is in my_tuple tuple collection
print('b' not in my_tuple)  # False,

numbers_tuple = (10, 20, 30, 40, 50)
print(min(numbers_tuple))  # 10
print(max(numbers_tuple))  # 50
print(sum(numbers_tuple))  # 150

# List
# index    0   1   2   3   4   5   6   7   8   9
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(my_list)
print(my_list[0])

# indexing operator, indexes, work exactly the same as with tuples
print(type(my_tuple), type(my_list))

my_list[0] = 11  # replace
print(my_list)  # [11, 20, 30, 40, 50, 60, 70, 80, 90, 100]

my_list.append(110)  # adds element at the of the list
print(my_list)  # [11, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

my_list.insert(1, 12)  # insert 12 on index 1, move all elements
print(my_list)  # [11, 12, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

my_list.extend([120, 130, 140])  # add elements from the argument to the end of the list
print(my_list)  # [11, 12, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]

my_list[0:2] = [1, 2]
print(my_list)  # [1, 2, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]

my_list[0:2] = [1, 2, 3]
print(my_list)  # [1, 2, 3, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]

del my_list[0]
print(my_list)  # [2, 3, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]

del my_list[0:2]
print(my_list)  # [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]

my_list.remove(140)
print(my_list)  # [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

my_list = [50, 2, 15, -10]
print(my_list)
my_list.sort()  # .sort() changes the original list
print(my_list)
my_list.sort(reverse=True)
print(my_list)

print('How many elements we have: ', len(my_list))
print('Max index: ', len(my_list) - 1)

print('-' * 30)

# How to iterate through a collection, so we can do something with each collection element.
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 1 approach - iteration through a list with WHILE loop
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

print('-' * 30)

# 2 approach - iteration through a list with FOR loop
# For each number in my_list do the following operations:
# number - it's a temporary variable that python will use and put single value from the list
# then, will do the content of the for loop and once that is completed, he will take next
# value from the list and put this value into number variable and execute the content of the for loop.
# The name of the temporary variable in for loop is totally up to us, we can name it as we want
for number in my_list:
    print(number)

names = ['Tom', 'Mark', 'Ann', 'Peter']
for name in names:
    print(name, end='---')

print('after for loop')

# by default print arguments are separated by space
# and newline character is added after the last argument
print('Cat', 'Dog', 'Car')

# you can change that by setting sep and end arguments
print('Cat', 'Dog', 'Car', sep='|', end='---')
print()
print('-' * 30)

# we can iterate through tuples in the same way
my_tuple = (10, 'Piotr', True, 3.14)
for element in my_tuple:
    print(element)

print('-' * 30)

"""
range(start, stop - 1, step)
https://docs.python.org/3/library/stdtypes.html#ranges
"""

for number in range(12):  # from 0 to 11
    print(number)

print('-' * 10)

for number in range(-5, 6):
    print(number)

print('-' * 10)

for number in range(-5, 6, 2):
    print(number, end='===')
