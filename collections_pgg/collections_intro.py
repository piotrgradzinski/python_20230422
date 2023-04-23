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
