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
