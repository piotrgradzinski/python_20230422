"""
Write a program that counts the number of occurrences of each character in the string
given by the user.

1. We will create empty dictionary, where we will be counting letters.
2. Get the string from the user.
3. Iterate over the string and:
    - character does not exist in dictionary (there is no key) - add it with value 0
    - increment the value number by 1

dictionary
key  => value
letter => number of occurrences (int)

> To be or not to be
t = 3
o = 4
  = 5
b = 2
e = 2
r = 1
n = 1
"""
occurrences = {}
users_input = input('Provide your text: ')

# count the letters
for character in users_input.lower():
    if character not in occurrences:
        occurrences[character] = 0

    occurrences[character] += 1

# display the result
for character, number_of_occurrences in occurrences.items():
    print(f"{character} = {number_of_occurrences}")
