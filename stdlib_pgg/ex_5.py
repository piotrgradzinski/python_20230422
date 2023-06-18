"""
Write a program that loads employees from the employees.csv file and counts:
- total sum salaries
- average of salaries
"""

import csv

with open('employees.csv', encoding='utf-8') as file_handle:
    data = csv.DictReader(file_handle, delimiter=';')

    # salaries = [float(row['salary']) for row in data]
    salaries = []
    for row in data:
        print(row)
        salaries.append(float(row['salary']))

    salaries_sum = sum(salaries)
    salaries_average = salaries_sum / len(salaries)

    print(f"Salaries sum: {salaries_sum}")
    print(f"Salaries average: {salaries_average}")
