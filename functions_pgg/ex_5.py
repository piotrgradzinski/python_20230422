"""
Write a function that calculates the number of characters in a given string between
given characters.
The characters between which the counting is to take place should be arguments
with default values - `<` and `>` respectively. Parentheses can be nested and
can occur many times.
Characters between nested brackets are counted according to the nesting level.

Example of use:

count_chars('mary <had> a little lamb')
3

count_chars('mary [had [a]] little [lamb]', '[', ']')
10

count_chars('a<a<a<a>>>')
6

mary <had> a little lamb -> 3
      111

mary [had [a]] little [lamb]
      1111 1           1111
           1

a <a<a<a>>>   -> 6
   1 1 1
     1 1
       1

How we can do that?
1. Create a function with the following arguments:
- text
- start with default value '<'
- end with default value '>'
2. Define variables: occurrences and level - both initially set to 0
3. Create a for loop where you iterate over all the characters with if condition inside:
- if current character equals start sign, increase level by 1
- elif current character equals end sign, decrease level by 1
- elif level is greater than zero add level value to occurrences variable (+=)
4. Return occurrences variable
"""


def count_chars(text: str, start: str = '<', end: str = '>'):
    occurrences = 0
    level = 0
    for character in text:
        if character == start:
            level += 1
        elif character == end:
            level -= 1
        elif level > 0:
            occurrences += level

    return occurrences


def test_simple_check_count_chars():
    assert count_chars('mary <had> a little lamb') == 3
    assert count_chars('mary [had [a]] little [lamb]', '[', ']') == 10
    assert count_chars('a<a<a<a>>>') == 6
