"""
Implement the function that formats the given strings.
Example of use:
> string_format(
        'amount due $price PLN',
        'amount due $price gross',
        price=10,
)
'amount due 10 PLN\namount due 10 gross'

Plan
1. define a function (string_format) that has *args and **kwargs
2. in the function definition
3. make a list that holds the processed strings that will be returned from the function
4. iterate over the strings (*args)
      5. iterate over all the **kwargs - dictionary of param names (keys) and values
          6. iterate over all occurrences in the subtitle, look for $param
              and replace it with the value from the given iteration
      7. add the processed string to the list of processed strings
8. Join list of processed string with \n character and return it

Tests
- no substitution: Hello World! -> Hello World!
- two strings but no substitution
    'Hello World!', 'Hello Python' -> 'Hello World!\nHello Python'.
- string with substitution
    'Hi $first_name $last_name', first_name="John", last_name="Kowalski" -> 'Hi Jan Kowalski'
- param that is not used
    'Hello World', first name='Jan' -> 'Hello World'
- no param provided
    'Hello $first_name' -> 'Hello $first_name'
"""


def string_format(*args, **kwargs) -> str:
    result = []

    for base_string in args:
        for param_name, param_value in kwargs.items():
            base_string = base_string.replace(f'${param_name}', str(param_value))

        result.append(base_string)

    return '\n'.join(result)


print(string_format('Hello $first_name $last_name', 'Hi $first_name',
                    first_name='Piotr', last_name='GG'))

# HOMEWORK: prepare pytest test cases
