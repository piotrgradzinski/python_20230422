# Functions

# function definition
# this function does not accept any arguments nor return anything
def say_hi():
    print('Hi!')
    print('Hi again!')


# function execution
say_hi()


# function definition
# this function accepts 2 arguments and returns nothing
def say_hi_to_someone(first_name, last_name):
    # inside the function we can treat arguments as variables
    print(f"Hello {first_name} {last_name}!")


# function execution
say_hi_to_someone('Piotr', 'GG')

my_first_name = 'John'
my_last_name = 'Doe'
say_hi_to_someone(my_first_name, my_last_name)
# say_hi_to_someone(my_first_name, my_last_name)
# say_hi_to_someone('John', 'Doe')


# function definition
# function with arguments that returns something
def my_sum(number_1, number_2):
    # once python executes "return" statement he will exit the function
    # meaning nothing after "return" statement will be executed
    return number_1 + number_2
    print(result)  # This code is unreachable


# function execution
result = my_sum(10, 20)
print(result)


# function definition
# we can have several return statement in our function
# even though I can have several return statement in my function,
# only one will be executed
def greater_than_0(number):
    if number > 0:
        return True
    else:
        return False


# function execution
result = greater_than_0(-5)
print(result)

result = greater_than_0(10)
print(result)

print('-' * 30)


"""
When defining a function we can have arguments with a default value. 
Then when executing the function we don't have to provide arguments 
which have a default value. We can but it's not mandatory.
Important rule is that when defining function first we define mandatory arguments 
(those without a default value) and then arguments with a default value.
"""


def wrapper(text: str, start: str = '>>>', end: str = '<<<') -> str:
    return start + text + end


# In which ways we can pass arguments to functions?
# by using positional arguments - it's based on the position of the argument during function invocation/execution
# the order of the arguments matters
print(wrapper('To be or not be', '>>>', '<<<'))
print(wrapper('To be or not be'))
print(wrapper('To be or not be', '...'))
print(wrapper('To be or not be', '...', '!!!'))

# by using named arguments
# the order doesn't matter
print(wrapper(text='To be or not to be', start='@@@', end='&&&'))
print(wrapper(end='&&&', start='@@@', text='To be or not to be'))
print(wrapper(end='&&&', text='To be or not to be', start='@@@'))
print(wrapper(text='To be or not to be', end='@@@'))

# by mixing positional and named arguments
# With this approach we have to provide positional arguments first and
# then named arguments in any order we want
print(wrapper('To be or not to be', end='$$$'))

print('-' * 30)

# One line if

person = {
    # 'id': 123,
    'first_name': 'Piotr',
    'last_name': 'GG'
}

# standard approach
if 'id' in person:
    has_id = True
else:
    has_id = False

print(has_id)

"""
one-liner approach
some restrictions:
- we have to provide both values when condition evaluates to True and to False
- you can return anything you want
- for simple operations
- when having more operations to be done within certain code block (if/else) use a standard approach
"""
has_id = True if 'id' in person else False
print(has_id)

has_id = 'Exists' if 'id' in person else 'Missing'
print(has_id)

print('-' * 30)

"""
Something to bool conversion. 
We have quite a few functions that allow us to convert data types:
- int(3.14) - will convert float to int
- float() - to float
- bool() - to boolean: True, False
- str() - to string
- list() - to list
- etc.
"""

print(bool('Piotr'))  # str -> bool, True
print(bool(' '))  # str -> bool, True
print(bool(''))  # str -> bool, False
# empty string -> False, non-empty string -> True

print(bool(10))  # int -> bool, True
print(bool(-5))  # int -> bool, True
print(bool(0))  # int -> bool, False
# 0 -> False, anything else -> True

print(bool('0'))  # str -> bool, True

print(bool([1, 2, 3]))  # list -> bool, True
print(bool([]))  # list -> bool, False
# this applies to other collections as well

# in this case list is not empty
print(bool([None]))  # list -> bool, True

print(bool(None))  # None -> bool, False

print('-' * 30)

"""
Scopes

https://drive.google.com/file/d/1dy5IVxzkUautwfxYSwwy3R7LQNWmNePJ/view?usp=sharing
https://realpython.com/python-scope-legb-rule

Name lookup scopes:
- Built-in scope: https://docs.python.org/3/library/functions.html
    - Global (or module) scope
        - Enclosing (or nonlocal) scope
            - Local (or function) scope
"""

my_number = 1  # defined in a global scope


def outer():
    # enclosed / local scope
    print('Outer function')
    # when we remove the following line python will take my_number from the global scope
    my_number = 100  # this line creates a new variable in the local scope and variable from the global scope is not changed
    print(my_number)


print(my_number)  # 1
outer()
print(my_number)

print('-' * 30)

"""
We can create functions that can take any number of arguments.
*args - it's a tuple of all positional arguments
**kwargs - it's a dictionary where key is an argument name and value this argument value
https://realpython.com/python-kwargs-and-args/
"""
print('Piotr', 'test', 1, 3.14, True)


def counter(*args, **kwargs):
    print('args: ', args)
    print('kwargs: ', kwargs)


counter(1, 2, 3, 'Tom', 3.14)
counter(1, 2, 3, first_name='Piotr', last_name='GG')
counter(title='Book', id=123)


print('-' * 30)

my_list = [1, 2, 3]

print(my_list)
my_list.append(4)
print(my_list)

my_list.append([5, 6, 7])
print(my_list)

my_list.extend([8, 9, 10])
print(my_list)

my_list += [11, 12, 13]
print(my_list)

print('-' * 30)

my_list = [1, 2, 3]
print(isinstance(my_list, list))  # True
print(isinstance(my_list, int))  # False
print(isinstance(my_list, str))  # False
