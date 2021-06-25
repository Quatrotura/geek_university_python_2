import requests
from decimal import *

def currency_rates(currency):
	"""This function is designed to return the currency rate of input currency toward ROUBLE.
	Data is fetched from the official web-site of Central Bank of Russia"""

	"""Indicate currency international acronym to get the INPUT CURRENCY - ROUBLE rate"""

	"""Input argument must be of str class"""

	url = 'http://www.cbr.ru/scripts/XML_daily.asp'
	response = requests.get(url)
	currency = currency.upper()

	if currency.isalpha() == True and currency in response.text:
		currency_rate = response.text[response.text.find
		('<Value>', response.text.find(currency))+7:
		response.text.find('</Value>',response.text.find(currency))]

		if ',' in currency_rate:
			currency_rate = currency_rate.replace(',', '.')
		
		return Decimal(currency_rate)

print(currency_rates('USD'))
print(currency_rates('eUr'))
