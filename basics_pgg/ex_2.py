"""
Write a program calculating the amount due for the purchased goods
based on the price per kilogram and the number of kilograms purchased.
Use variables to store price and weight. Write all information to the console.

Sample program output:
Price per kg: 10.0
Weight: 2.5
Total price: 25.0
"""

price = 10.0
weight = 2.5
total_price = price * weight

# 1 approach
print('Price per kg:', price)
print('Weight:', weight)
print('Total price:', total_price)

# 2 approach
print('Price per kg: ' + str(price))
print('Weight: ' + str(weight))
print('Total price: ' + str(total_price))

# 3 approach
print(f'Price per kg: {price}')
print(f'Weight : {weight}')
print(f'Total price: {total_price}')
