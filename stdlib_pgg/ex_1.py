"""
Write a program to handle an employee database.
Store first name, last name, email, year of birth, salary in the database.

Make use of the json module.

Usage example:
What would you like to do? [a - add, l - list employees] a
First name: Jan
Last name: Nowak
Year of birth: 1980
Salary: 5000.0

What would you like to do? [a - add, l - list employees] l
- [1] Jan Nowak - year of birth: 1980, salary: 5000.00 PLN

How to do it?
- read the employees.json file
    if we are not able to read it - catch the error (exception) and create empty employee list
- ask for users action
    - perform the action: add or list
- if the action was add we have to save the file to disc
"""
import json

try:
    with open('employees.json', 'r', encoding='utf-8') as db_file:
        employees = json.load(db_file)
except FileNotFoundError:
    employees = []

action = input('What would you like to do? [a - add, l - list employees]: ')

if action == 'a':
    ...
elif action == 'l':
    ...
