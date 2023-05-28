"""
Write a program that loads a list of email addresses from a file and creates a new file with
the filtered content.
The input file may contain duplicate addresses, the same address written in different case,
lines containing whitespace characters and invalid email addresses (the @ sign is missing or
occurs multiple times).
The resulting file should contain unique, sorted, valid email addresses.

for each email:
- is the email valid - contains only one @
- make all letters in the email lowercase
- remove non-printable characters (.strip(), .replace() - to remove spaces)
"""

emails = set()
with open('emails.txt', 'r', encoding='utf-8') as file_handle:
    for line in file_handle:
        if line.count('@') != 1:  # check the number of @
            continue

        # clean the line - remove non-printable characters, make all letters lowercase
        email_address = line.strip().replace(' ', '').lower()

        emails.add(email_address)  # add to set

# sort
from natsort import natsorted
sorted_emails = natsorted(emails)

# write cleaned emails to a separate file
with open('cleaned_emails.txt', 'w') as file_handle:
    for email in sorted_emails:
        file_handle.write(email)
        file_handle.write('\n')
