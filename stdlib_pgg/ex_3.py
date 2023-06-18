"""
Based on the urls.txt file extract unique domain names.

regexp: ^https?://(www\.)?([^/]+)/.*

- create an empty set to store the domains
- read the file
- for each line apply regular expression, retrieve the domain name from 2 group
- add this match to domains set
- display the results
"""

