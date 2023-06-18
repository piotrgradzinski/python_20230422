"""
Using NBP endpoint http://api.nbp.pl/api/exchangerates/tables/A/?format=json
fetch the information about current exchange rates
and display the information to the user:
currency code - rate

for example
EUR - 4.4583
"""
import requests

url = "http://api.nbp.pl/api/exchangerates/tables/A/?format=json"

exchange_rates = requests.get(url).json()

for rate in exchange_rates[0]['rates']:
    print(rate['code'], '-', rate['mid'])
