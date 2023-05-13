"""
Write a program that counts the number of occurrences of vowels
(`a, e, i, o, u, y`) in the string given by the user.

1. Use input function to get the string from the user
2. Iterate over that string using for loop
3. Check if particular letter is in the list of vowels, if so, count the letter.

What we can do with uppercase letters?
1. We can add them to the vowels list.
2. We can use .lower() method.
"""

users_input = input('Provide a string: ')  # To Be Or Not TO be

vowels = ['a', 'e', 'y', 'u', 'i', 'o']
counter = 0

for character in users_input:
    if character.lower() in vowels:
        counter += 1

print(f'Within "{users_input}" we have {counter} vowels.')
