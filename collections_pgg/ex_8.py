"""
Write a program calculating the total amount due for the purchased goods based
on the weight and product name provided by the user.
To store price information per kilogram of the products use a dictionary.
List all available products in the store.

How we can do that?
1. Create a dictionary with products, lets add:
    potatoes - 1.2
    tomatoes - 4.5
    carrots - 0.5
2. Print the dictionary
3. Ask the user about the product and check if is available in our dictionary
4. Ask how many kilograms user wants to buy
5. Calculate users due
"""

products = {
    'potatoes': 1.2,
    'tomatoes': 4.5,
    'carrots': 0.5,
}

for product, price in products.items():
    print(f"{product} - {price:.2f} PLN / kg")

product_name = input("What would you like to buy? ")

if product_name not in products:
    print("We don't have anything like that. Sorry!")
    exit()  # "stop", don't do anything else

weight = float(input(f"How many kilograms of {product_name} would you like to buy? "))

due = products[product_name] * weight
print(f"For {weight} kg of {product_name} you have to pay {due:.2f} PLN")
