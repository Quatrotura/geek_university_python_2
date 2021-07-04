# *(вместо 3) Решить задачу 3 для ситуации, 
# когда объём данных в файлах превышает объём ОЗУ (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта). 
# Только теперь не нужно создавать словарь с данными. Вместо этого нужно сохранить объединенные данные в новый файл (users_hobby.txt). 
# Хобби пишем через двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None. 
# Если наоборот — выходим из скрипта с кодом «1». 

from itertools import zip_longest

with open('users.csv', 'r', encoding = "utf-8") as user:
	with open('hobby.csv', 'r', encoding = 'utf-8') as hobby:
		with open('users_hobby.txt', 'w+', encoding = 'utf-8') as user_hobby:
			for user_line, hobby_line in zip_longest(user, hobby, fillvalue = None):
				if user_line != None:
					user_line = user_line.replace("\n", "")
					recoding_line = f'{user_line}: {hobby_line}'
					user_hobby.write(recoding_line)
				else:
					# user_hobby.seek(0)
					# print(user_hobby.read())
					exit(1)

			user_hobby.seek(0)
			print(user_hobby.read())