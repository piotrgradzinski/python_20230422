"""
Pickle

Is a build in format in python for data storage (serialization and deserialization).
https://docs.python.org/3/library/pickle.html?highlight=pickle#module-pickle
"""

import pickle

data = {
    'year': 2020,
    'students': [
        {
            'first_name': 'John',
            'last_name': 'Doe'
        },
        {
            'first_name': 'Ann',
            'last_name': 'Kowalski'
        }
    ]
}

pickle.dump(data, open('data.p', 'wb'))

"""
Data format are (most of the time) language independent.
!!!
Java != JavaScript
!!!


JSON - JavaScript Object Notation
Data format is derived from JavaScript.
Important to know that it's a separate data format. 
It may look similar to Python structures (like dictionaries or lists)
but it's not the same and has some limitations. 

There are some signification differences between Python structures and JSON structures:
Python - JSON
dict - object
list - array
True/False - true/false
None - null
tuple() - there is no tuple structure in JSON
set() - there is no set structure in JSON

https://en.wikipedia.org/wiki/JSON
"""

data = {
    'year': 2020,
    'students': [
        {
            'first_name': 'John',
            'last_name': 'Doe'
        },
        {
            'first_name': 'Ann',
            'last_name': 'Kowalski'
        }
    ],
    'available': True,
    'is_connected': None,
}

import json

"""
Within json module we have:
- dumps - will return a string in a JSON format
- dump - will write the data in a JSON to a file
- loads - converts JSON data into Python data from a string
- load - converts JSON data into Python data from a file
"""

print(json.dumps(data, indent=4))  # indent - makes indentations, so JSON looks better and is more readable

json.dump(data, open('data.json', 'w'), indent=4)

data = json.loads('{"course": "Python"}')
print(data)

data = json.load(open('employees.json'))
print(data)
