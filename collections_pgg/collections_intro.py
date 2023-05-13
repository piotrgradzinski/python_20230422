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

print()
print('-' * 30)

# We can use nested for loops
for a in range(1, 11):
    for b in range(1, 11):
        print(f'{a}+{b}={a+b}')

print('-' * 30)
a = 10
b = 4
print(f"{a*b:4}")

print('-' * 30)

# index: 0      1      2        3
names = ['Tom', 'Ann', 'Piotr', 'Mary']
# with this approach we have access to values only, not to an index
for name in names:
    print(name)

print('-' * 10)

"""
To be able to access both index and value
we can use enumerate function that will
return both index and value.

Enumerate for each element in a collection
returns a tuple with number (index) and value.
"""

names = ['Tom', 'Ann', 'Piotr', 'Mary']
for index, name in enumerate(names):
    print(index, name)

print('-' * 10)

names = ['Tom', 'Ann', 'Piotr', 'Mary']
for index, name in enumerate(names, start=10):
    print(f"{index}. {name}")

print('-' * 10)

"""
Unpacking - works with any collection
The number of elements on both sides needs to match,
otherwise we will have an error.
"""
first_name, last_name = ('Piotr', 'GG')
print(first_name)
print(last_name)

print('-' * 10)

names = ['Tom', 'Ann', 'Piotr', 'Mary']
for index, name in enumerate(names):
    print(index, name)

print('-' * 3)

# with range
names = ['Tom', 'Ann', 'Piotr', 'Mary']
for index in range(0, len(names)):
    print(index, names[index])

print('-' * 30)

"""
STRINGS
We can treat them as collections of characters.
Strings are immutable.
"""

#            0123456789...
my_string = 'To be or not to be'

# we can use indexing operator
print(my_string[0])  # T
print(my_string[1])  # o
print(my_string[2])  # space
print(my_string[1:4])  # o b
print(my_string[-1])  # e
print(my_string[::2])  # T eo o ob
print(my_string[::-1])  # eb ot ton ro eb oT

# we have string specific operations
# the result of every operation is a new string
print(my_string)  # To be or not to be
print(my_string.lower())  # to be or not to be
print(my_string.upper())  # TO BE OR NOT TO BE
print(my_string.title())  # To Be Or Not To Be
print(my_string.capitalize())  # To be or not to be

sentence = 'my name is piotr. how do you do?'
print(sentence.capitalize())  # My name is piotr. how do you do?

"""
We can split a string into chunks.
.split() method returns a list of chunks.
"""
print(my_string.split())  # by default split uses spaces as a separator
print(my_string.split(' '))
print(my_string.split('o'))
print(my_string.split('be'))

for word in my_string.split(' '):
    print(word)

# we can join strings together as well

names = ['Tom', 'Ann', 'Piotr', 'Mary']
# take <-> as a glue that will connect string from names list and return new string
print('<->'.join(names))  # Tom<->Ann<->Piotr<->Mary

print(my_string)
print(my_string.count('o'))  # 4
print(len(my_string))  # 18
print('to' in my_string)  # True
print('Piotr' in my_string)  # False

# To and to - those are two different strings!
print(my_string.find('to'))  # 13 - returns the first index where the string we are looking for starts
print(my_string.find('Piotr'))  # -1 - returns -1 if substring was not found

print(my_string.index('to'))  # 13
# If substring is not found then the ValueError exception is thrown.
# print(my_string.index('Piotr'))

print(my_string.replace('o', '*'))

print('-' * 3)

for character in my_string:
    print(character)

print('-' * 30)

"""
Dictionary
"""
# key: value
my_dict = {
    'first_name': 'Piotr',
    'last_name': 'GG',
    'shoe_number': 46,
    'works_at_ALX': True,
    'favourite_numbers': [10, 20, 30]
}

print(my_dict)

# getting elements via indexing operator
# indexing operator to access elements
print(my_dict['first_name'])
print(my_dict['shoe_number'])
print(my_dict['favourite_numbers'])
# print(my_dict['height'])  # KeyError: 'height'

# setting/adding elements
my_dict['first_name'] = 'Mark'
print(my_dict)
my_dict['weight'] = 90
print(my_dict)

# getting elements via .get() method
print(my_dict.get('first_name'))
"""
For keys that are not present in a dictionary get will return None 
instead of raising a KeyError exception as indexing operator does
"""
print(my_dict.get('height'))

# with .get() method we can define default value to be returned if the key is not present
print(my_dict.get('height', 0))

my_dict = {
    'first_name': 'Piotr',
    0: 3.14,
    2.5: 'Two and a half',
    (1, 2): 'Tuple',
    # [10, 20]: 'List',  # TypeError: unhashable type: 'list'
}
print(my_dict)
print(my_dict['first_name'])
print(my_dict[0])
print(my_dict[2.5])
print(my_dict[(1, 2)])

del my_dict['first_name']
print(my_dict)

print('-' * 30)

my_dict = {
    'first_name': 'Piotr',
    'last_name': 'GG',
    'shoe_number': 46,
    'works_at_ALX': True,
    'favourite_numbers': [10, 20, 30]
}

# by default, we iterate through keys
for key in my_dict:
    print(key, my_dict[key])

print('-' * 30)

"""
Dictionaries are able to expose different ways
of iterating through its elements.
We have 3 special methods that will allow us to iterate through a dictionary in different ways:
- .keys() - a default way of iterating through a dictionary
- .values()
- .items()
"""

for key in my_dict.keys():
    print(key)

print('-' * 3)

for value in my_dict.values():
    print(value)

print('-' * 3)

for key, value in my_dict.items():
    print(key, value)

print('-' * 30)

print('first_name' in my_dict)
print('address' in my_dict)

print('-' * 30)

"""
Sets
"""

# empty set
my_set = {}  # Warning! This is an empty dict! Not set!
print(type(my_set))

my_set = set()
print(type(my_set))


my_set = {10, 20, 30, 40, 50}

print(type(my_set))
print(my_set)  # {50, 20, 40, 10, 30}

my_set.add(50)  # only unique elements
print(my_set)  # {50, 20, 40, 10, 60, 30}

my_set.add(60)
print(my_set)  # {50, 20, 40, 10, 60, 30}

my_set.remove(60)
print(my_set)

my_set.update({1, 2, 3})
print(my_set)

my_set.add('Piotr')
my_set.add(3.14)
my_set.add(True)
my_set.add(None)
my_set.add((10, 20, 30))
# my_set.add([1, 2, 3])  # TypeError: unhashable type: 'list'
print(my_set)

print('-' * 30)

for element in my_set:
    print(element)

# indexing operator will not work...
# print(my_set[0])  # TypeError: 'set' object is not subscriptable

print('-' * 30)

# Set theory operations
# https://piotr.gg/sql/sql-joins.html

a = {1, 2, 3}
b = {1, 2, 4, 5}

# Union, sum
print(a.union(b))  # {1, 2, 3, 4, 5}
print(a | b)

# Intersection
print(a.intersection(b))  # {1, 2}
print(a & b)

# Difference, subtraction - from a subtracking b
print(a.difference(b))  # {3}
print(a - b)

# Symmetric difference
# from union of two sets subtract intersection
print(a.symmetric_difference(b))  # {3, 4, 5}
print(a ^ b)

# We can test sets
# Is disjoint? Don't have any common part (no intersection).
print(a)  # {1, 2, 3}
print(b)  # {1, 2, 4, 5}
print(a.isdisjoint(b))  # False

"""
What is a subset?
For example, {1, 2} is a subset of {1, 2, 3}, and so is {2} but {1, 4} is not.
"""

# Is A a subset of B? Sets can't be the same.
print(a < b)  # False

c = {1, 2}
print(c < a)

# Is C a subset of A? Sets CAN be the same.
print(c <= a)

print(a)  # {1, 2, 3}
print(b)  # {1, 2, 4, 5}
print(a < b)  # False
print(b < a)  # False

print('-' * 30)

# One way of using sets is to get rid of the duplicated values
# here we have list of names, and some names are duplicated
names = ['Piotr', 'Tom', 'Mark', 'Tom', 'Piotr', 'Tom']
print(names)

"""
In Python it's really simple to convert one collection
into another. Just need to use desired collection and pass the data 
"""

# list -> set conversion
names_set = set(names)
print(names_set)

# set -> list conversion
names = list(names_set)
print(names)
