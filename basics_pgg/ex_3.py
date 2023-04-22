"""
Write a program that calculates the cost of travel from city A to city B
based on the number of kilometers given by the user, the price of fuel
and fuel consumption. Ask the user for the cities names.

Use a proportion formula to calculate this:
cost = distance * fuel_consumption / 100.0 * price
cost = 420 * 5.5 / 100.0 * 4.55

Sample program input:
City A: Warsaw
City B: Gdańsk
Distance Warsaw-Gdansk: 420
Fuel price for 1l: 4.55
Fuel consumption per 100 km: 5.5

Sample program output:
The cost of the Warsaw-Gdańsk journey is 105.11 PLN
"""

city_a = input('City A: ')
city_b = input('City B: ')
distance = int(input(f'Distance {city_a}-{city_b}: '))
price = float(input('Fuel price: '))
fuel_consumption = float(input('Fuel consumption per 100 km: '))

cost = distance * fuel_consumption / 100.0 * price

print(f'The cost of the {city_a}-{city_b} journey is {cost} PLN')

# quite often for the display purpose we'd like to format numbers
# 1 approach
print(f'The cost of the {city_a}-{city_b} journey is {round(cost, 2)} PLN')

# 2 approach - leverage f-string formatting
print(f'The cost of the {city_a}-{city_b} journey is {cost:.2f} PLN')
