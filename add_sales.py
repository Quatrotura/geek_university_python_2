from sys import argv

def add_sales(argv):
	"""This function writes into bakery.css the amount of sales input
	by the user in the terminal. Input value shall be of number type only"""

	trash, sales_value = argv
	with open('bakery.csv', 'a', encoding='utf-8') as f_recoder:
		sales_record = sales_value + '\n'
		f_recoder.write(sales_record)
		print(sales_value)

add_sales(argv)
