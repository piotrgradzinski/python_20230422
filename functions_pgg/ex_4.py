"""
Write a function that returns a set of all characters appearing
more than a given number of times in a string.

Example of use:
more_than('mary had a little lamb', 3)
{'a', ' '}

1. Define function
2. Count the number of characters in a string into a dictionary
3. Go through this dictionary and if the number is greater than the number in second argument, add it to set.
4. Return the set

Test cases:
empty string
non-empty string
a string with small/big letters
"""


def more_than(text: str, occurrences: int) -> set:
    """
    Returns a set of characters that appear in text more than certain number of times.
    :param text:
    :param occurrences: At least how many times a character should appear in the text to be returned in the set.
    :return:
    """
    text = text.lower()
    characters_count = dict()  # or {} - this expression creates an empty dictionary
    results = set()

    for character in text:
        if character not in characters_count:
            characters_count[character] = 0
        characters_count[character] += 1

    for character, character_occurrences in characters_count.items():
        if character_occurrences > occurrences:
            results.add(character)

    return results


def test_empty_text():
    assert more_than('', 0) == set()


def test_non_empty_text():
    assert more_than('aaaabbbccd', 2) == {'a', 'b'}


def test_lower_capital_letters():
    assert more_than('BBBBBbbbbbAAaaCcdD', 2) == {'a', 'b'}
