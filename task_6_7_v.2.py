from sys import argv

def change_sales(argv):

	trash, *change_args = argv
	line_count = 0
	if len(argv) == 3:
		with open('bakery.csv', 'r', encoding = 'utf-8') as f_main:
			with open('bakery_copy.csv', 'w', encoding = 'utf-8') as f_copy:
				for line in f_main:
					line_count +=1
					if line_count == int(change_args[0]):
						f_copy.write(change_args[1]+'\n')
					else:
						f_copy.write(line)
				if line_count < int(change_args[0]):
					print("Номера введенной строки не существует.\n\
Если хотите добавить новое значение, используйте фукнцию add_sales.py")
	else:
		print('Введите данные в формате: [номер строки] [перезаписываемая сумма]')
		exit(1)

	with open('bakery.csv', 'w+', encoding = 'utf-8') as f_main:
		with open('bakery_copy.csv', 'r', encoding = 'utf-8') as f_copy:
			for line in f_copy:
				f_main.write(line)
			exit(0)

change_sales(argv)
