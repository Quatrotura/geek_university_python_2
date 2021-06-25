import requests.api
from datetime import datetime

def currency_rates(currency):
	"""This function is designed to return the currency rate of input currency toward ROUBLE.
	Data is fetched from the official web-site of Central Bank of Russia"""

	"""Indicate currency international acronym to get the INPUT CURRENCY - ROUBLE rate"""

	"""Input argument must be of str class"""

	url = 'http://www.cbr.ru/scripts/XML_daily.asp'
	response = requests.get(url)
	currency = currency.upper()

	rate_date = response.text[response.text.find('ValCurs Date')+len('ValCurs Date="'):
	response.text.find('ValCurs Date')+len('ValCurs Date="')+10]

	if currency.isalpha() == True and currency in response.text:
		currency_rate = response.text[response.text.find
		('<Value>', response.text.find(currency))+7:
		response.text.find('</Value>',response.text.find(currency))]

		if ',' in currency_rate:
			currency_rate = currency_rate.replace(',', '.')
		answer = f'{currency_rate}, {rate_date}'
		return answer

# проверочка
# print(currency_rates('usd'))
