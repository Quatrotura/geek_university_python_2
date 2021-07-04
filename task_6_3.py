# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби. 
# Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая. 
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. 
# Сохранить словарь в файл. Проверить сохранённые данные. 
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None. 
# Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.

import itertools

names = []
hobbies = []
users = {}

with open('users.csv', 'r', encoding = "utf-8") as user:
	with open('hobby.csv', 'r', encoding = 'utf-8') as hobby:
		names = [" ".join(line.split(',')) for line in user.read().splitlines()]
		hobbies = [', '.join(line.split(',')) for line in hobby.read().splitlines()]

# users = {key: value for key,value in itertools.zip_longest(names, hobbies, fillvalue=None)}

for key,value in itertools.zip_longest(names, hobbies, fillvalue=None):
	if key != None:
		users.setdefault(key,value)
	else:
		with open('names_hobbies.txt', 'w', encoding = 'utf-8') as f:
			f.write(str(users))
		# print(users)
		exit(1)

with open('names_hobbies.txt', 'w', encoding = 'utf-8') as f:
	f.write(str(users))

print(users)
