"""
Find all dates in dates.txt file that are in a format YEAR-MONTH-DAY,
ex. 2023-06-18 and print the results.
"""

with open('dates.txt', encoding='utf=8') as file_handle:
    content = file_handle.read()
