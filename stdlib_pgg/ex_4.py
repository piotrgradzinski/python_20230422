"""
Using dates.txt change the date format
from 1914-10-20
to 20.10.1914
"""
import re

with open('dates.txt', encoding='utf-8') as file_handle:
    content = file_handle.read()

    new_content = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3.\2.\1", content)

    print(content)
    print(new_content)

    # replacing *Belgian* with <strong>Belgian</strong>
    # *? - lazy quantifier
    new_content = re.sub(r"\*(.*?)\*", r"<strong>\1</strong>", content)
    print(new_content)

    new_content = re.sub(r"\*([^*]+)\*", r"<strong>\1</strong>", content)
    print(new_content)
