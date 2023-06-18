"""
Based on the urls.txt file extract unique domain names.

regexp: ^https?://(www\.)?([^/]+)/.*

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

    for domain in domains:
        print(domain)
