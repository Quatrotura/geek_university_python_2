# *(вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему номер записи и новое значение. 
# При этом файл не должен читаться целиком — обязательное требование. 
# Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.

from sys import argv

def change_sales(argv):

	trash, *change_args = argv
	if len(argv) == 3:
		with open('bakery.csv', 'r', encoding = 'utf-8') as f_read:
			lines = [line.rstrip() for line in f_read]

		if len(lines) >= int(change_args[0]):
			lines[int(change_args[0])-1] = change_args[1]
			with open('bakery.csv', 'w', encoding = 'utf-8') as f_write:							
				for line in lines:
					f_write.write(line+'\n')
		else:
				print("Номера введенной строки не существует.\n\
Если хотите добавить новое значение, используйте фукнцию add_sales.py")

	else:
		print('Введите данные в формате: [номер строки] [перезаписываемая сумма]')
		exit(0)


change_sales(argv)


# for i in range(int(change_args[0])-1):
# 	lines_len += len(f.readline())
# lines_len = 0
# req_line = ''
# diff = 0
# req_line = f.readline()
# diff = len(req_line) - 1 - len(change_args[1])
# print('differnce in len', diff)

# f.seek(lines_len, 0)
# print(f.tell())

# f.write(change_args[1])
# # if diff > 0:
# # 	for demolish in range(diff):
# # 		f.write('\0')