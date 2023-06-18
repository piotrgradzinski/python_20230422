"""
Find all dates in dates.txt file that are in a format YEAR-MONTH-DAY,
ex. 2023-06-18 and print the results.
"""
import re

with open('dates.txt', encoding='utf=8') as file_handle:
    content = file_handle.read()

    results = re.findall(r"\d{4}-\d{2}-\d{2}", content)
    print(results)
    for result in results:
        print(result)
