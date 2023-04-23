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

exit()
# you can't modify the tuple after its creation
# my_tuple[0] = 1000  # TypeError: 'tuple' object does not support item assignment

print(len(my_tuple))  # length of the collection, how many elements we have in a collection
print('a' in my_tuple)  # True, checks if 'a' is in my_tuple tuple collection
print('b' not in my_tuple)  # False,

numbers_tuple = (10, 20, 30, 40, 50)
print(min(numbers_tuple))  # 10
print(max(numbers_tuple))  # 50
print(sum(numbers_tuple))  # 150
