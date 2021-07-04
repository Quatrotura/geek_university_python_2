# Реализовать простую систему хранения данных о суммах продаж булочной. 
# Должно быть два скрипта с интерфейсом командной строки: для записи данных и для вывода на экран записанных данных. 
# При записи передавать из командной строки значение суммы продаж. Для чтения данных реализовать в командной строке следующую логику:
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. 



# Женя, это общий файл со всеми функциями задания 6
# В реквесте также есть отдельные файлы с функциями: add_sales.py и show_sales.py

from sys import argv

def add_sales(argv):
	"""This function writes into bakery.css the amount of sales input
	by the user in the terminal. Input value shall be of number type only"""
	trash, sales_value = argv
	with open('bakery.csv', 'a', encoding='utf-8') as f_recoder:
		sales_record = sales_value + '\n'
		f_recoder.write(sales_record)
		print(sales_value)

# add_sales(argv)

def show_sales(argv):
	"""This function return sales amounts"""
	trash, *sales_idx = argv

	with open('bakery.csv', 'r', encoding = 'utf-8') as f:		
		if len(argv) == 1:			
			for line in f:
				print(line.rstrip())		
			exit(0)

		for i in range(int(sales_idx[0])-1):
			f.readline()

		if len(sales_idx) == 1:
			for line in f:
				print(line.rstrip())		
		elif len(sales_idx) == 2:
			lines_req = int(sales_idx[1]) - int(sales_idx[0]) + 1
			for i in range(lines_req):
				print(f.readline().rstrip())
		else:
			print("You've entered something wrong! Try again.")
			exit(1)
			
show_sales(argv)
