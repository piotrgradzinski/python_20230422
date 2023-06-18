"""
VAT taxpayer list API

Write a program that will check the VAT taxpayer list for information about a company
based on its VAT number.

Use https://wl-api.mf.gov.pl/api/search/nip/{VATID}?date=2023-06-18 endpoint where {VATID}
has to be replaced with VAT ID of the company.

For example:
https://wl-api.mf.gov.pl/api/search/nip/5272642198?date=2023-06-18

Documentation
https://wl-api.mf.gov.pl/#nip?date
"""
import requests
import datetime

vat_id = input('Provide VAT ID (NIP): ')

current_date = datetime.datetime.now().strftime("%Y-%m-%d")
url = f"https://wl-api.mf.gov.pl/api/search/nip/{vat_id}?date={current_date}"

response = requests.get(url).json()
company_data = response['result']['subject']

print(f"Company name: {company_data['name']}")
print(f"VAT ID: {company_data['nip']}")
print(f"Address: {company_data['workingAddress']}")
print(f"Status: {company_data['statusVat']}")
