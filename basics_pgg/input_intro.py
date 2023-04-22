# input, getting information from the user


first_name = input('Provide you first name: ')
print(f'Thank you {first_name}!')
print(type(first_name))

# input function ALWAYS returns a string!
# input function DOES NOT convert strings to numbers
# we have to do it on our own!

age = input('Provide your age: ')
new_age = age * 10
print(f'Your age: {age}, {new_age}')

# to avoid this kind of problem we have to convert the input data
age = input('Provide your age: ')
age = float(age)
new_age = age * 10
print(f'Your age: {age}, {new_age}')

# instead of dividing input and conversion to separate lines
# we can do that in one line
age = float(input('Provide your age: '))
new_age = age * 10
print(f'Your age: {age}, {new_age}')
