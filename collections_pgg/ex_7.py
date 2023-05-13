"""
Write a program that counts the number of characters between the brackets `<>`
in the string given by the user. Assume that there is only one pair of brackets.

Example:
Mary had a <little> lamb
6

0123456
To <be> or not to be
2

How we can do that?
Approach 1
1. Check the occurrences number of < and > - we should have only one for each one.
    Otherwise, stop the program using exit() function.
2. Iterating over the string and checking, if:
      - should I start counting
      - should I stop counting
      - if the counting is on

Approach 2
1. Check the occurrences number of < and > - we should have only one for each one.
    Otherwise, stop the program using exit() function.
2. Get the index of >
3. Get the index of <
4. Subtract them and subtract 1.
"""