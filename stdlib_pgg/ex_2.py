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

    print('-' * 30)

    results = re.findall(r"(\d{4})-(\d{2})-(\d{2})", content)
    print(results)

    print('-' * 30)

    results = re.findall(r"((\d{4})-(\d{2})-(\d{2}))", content)
    print(results)

    print('-' * 30)

    for match in re.finditer(r"((\d{4})-(\d{2})-(\d{2}))", content):
        print(match)
        print(match.groups())
        print(match.group(1), match.group(2))

    print('-' * 30)

    # .search will return first match
    result = re.search(r"((\d{4})-(\d{2})-(\d{2}))", content)
    print(result)

    print('-' * 30)

    # .match - Try to apply the pattern at the start of the string
    result = re.match(r"((\d{4})-(\d{2})-(\d{2}))", content)
    print(result)
