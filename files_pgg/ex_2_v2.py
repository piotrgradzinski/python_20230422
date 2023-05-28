"""
Write a programme that will read the log file with users activity in the system.
Display the information of how much time user spent in the system as the sum of
numbers read from the file.

Sample output:
Time spent in the system:
user-1: 100 s
user-2: 12352 s
...

Plan
- to store the information about the time spent by a user in a system we can use
dictionary or defaultdict where the key would be user name/id and value time spent in the system
- read file line by line (ex. using for loop)
- parse the line (.split()) - extracting user name / id and number of seconds (convert the second one to int)
- add this information to the dictionary
"""

from collections import defaultdict

total_time = defaultdict(int)
with open('logs_simple.txt', 'r', encoding='utf-8') as file_handle:
    for line in file_handle:
        try:
            user_name, time_spent = line.split(';')
            total_time[user_name] += int(time_spent)
        except ValueError:
            continue

print('Time spent in the system')
for user_name, time_spent in total_time.items():
    print(f'{user_name}: {time_spent} s')

print('-' * 30)

"""
Improvement - having the list sorted. 
Sorting dictionaries is a bit cumbersome... 
"""
for user_name in sorted(total_time.keys()):
    print(f'{user_name}: {total_time[user_name]} s')

print('-' * 30)

"""
- open terminal 
- execute: pip install natsort
"""
from natsort import natsorted

for user_name in natsorted(total_time.keys()):
    print(f'{user_name}: {total_time[user_name]} s')
