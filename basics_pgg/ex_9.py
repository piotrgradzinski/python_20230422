"""
Write a program that calculates the average temperature
for a given week based on temperatures entered by the user.

- create temperature_sum variable = 0
- using the while ask user 7 times to provide a temperature reading
- after the while loop calculate the average by dividing
  the sum of temperatures by 7
- display the results
"""

day_number = 1
temperature_sum = 0

while day_number <= 7:
    temperature_sum += float(input(f'Provide temperature for day {day_number}: '))
    day_number += 1

average_temperature = temperature_sum / 7

print(f'Average temperature is {average_temperature:.2f}')
