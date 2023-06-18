"""
Dates

https://realpython.com/python-datetime/
https://realpython.com/python-packages/#dateutil-for-working-with-dates-and-times

Within datetime package we have:
- time
- date
- datetime
"""

import datetime

d = datetime.date(year=2023, month=6, day=18)
print(d)

t = datetime.time(hour=16, minute=37, second=0)
print(t)

dt = datetime.datetime(year=2023, month=6, day=18, hour=16, minute=37, second=0)
print(dt)

dt = datetime.datetime.now()
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)
print(dt.weekday())  # 0 = Monday, 6 = Sunday
print(dt.isoweekday())  # 1 = Monday, 7 = Sunday

"""
Converting datetime object into a string with given format.
"""
print(dt.isoformat())

"""
to convert the datetime object to fit our needs 
we can use method strftime()
strftime -> string from time
full list of available tokens: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
"""

print(dt.strftime('%d.%m.%Y %H:%M:%S'))

"""
convert string/number into a datetime object
- timestamp, epoch 01.01.1970 00:00:00
- iso format
- strptime() - string parse time
"""
# https://www.epochconverter.com/
dt = datetime.datetime.fromtimestamp(1687099708)
print(dt)

dt = datetime.datetime.fromisoformat('2023-03-01T12:10:23')
print(dt)

dt = datetime.datetime.strptime("24.01.2023 13:10:44", "%d.%m.%Y %H:%M:%S")
print(dt)
