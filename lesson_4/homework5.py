from homework2 import currency_rates
from datetime import date

command = input('название валюты: ')
print(currency_rates(command), date.today())