"""
Implement a function that flattens the given list.

Example:
> flatten([1, 2, 3, [4, 5, [6]], 7])
[1, 2, 3, 4, 5, 6, 7]

Plan
1. Create an empty list, which we will fill with elements (e.g. result = [])
2. Loop through all the elements in the list using a for loop
  - if the element we are processing is a list
      run the flatten function for this element and add the result to the result variable (+= or .extend())
  - if the element we are processing is NOT a list:
      we add it to the list result (.append())
"""


def flatten(data: list) -> list:
    ...

