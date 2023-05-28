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
- parse the line - extracting user name / id and number of seconds (convert the second one to int)
- add this information to the dictionary
"""
