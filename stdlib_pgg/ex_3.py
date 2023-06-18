"""
Based on the urls.txt file extract unique domain names.

regexp: ^https?://(www\.)?([^/]+)/.*
visualization: https://regexper.com/#%5Ehttps%3F%3A%5C%2F%5C%2F%28www%5C.%29%3F%28%5B%5E%2F%5D%2B%29%5C%2F.*

- create an empty set to store the domains
- read the file
- for each line apply regular expression (re.search), retrieve the domain name from 2 group
- add this match to domains set
- display the results
"""
import re

with open('urls.txt', encoding='utf-8') as file_handle:
    domains = set()
    for line in file_handle:
        address = line.strip().lower()
        result = re.search(r"^https?://(www\.)?([^/]+)/.*", address)
        domain = result.group(2)
        domains.add(domain)

    for domain in sorted(domains):
        print(domain)
