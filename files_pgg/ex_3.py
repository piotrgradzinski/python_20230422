"""
Write a program that loads a list of email addresses from a file and creates a new file with
the filtered content.
The input file may contain duplicate addresses, the same address written in different case,
lines containing whitespace characters and invalid email addresses (the @ sign is missing or
occurs multiple times).
The resulting file should contain unique, sorted, valid email addresses.

for each email:
- is the email valid - contains only one @
- make all letters in the email lowercase
- remove non-printable characters (.strip(), .replace() - to remove spaces)
"""

