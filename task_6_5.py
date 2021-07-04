# **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, 
# чтобы можно было задать имя обоих исходных файлов и имя выходного файла. 
# Проверить работу скрипта.

from itertools import zip_longest
from sys import argv

def write_names_hobbies(argv):
	trash, users, hobbies, users_hobbies = argv
	with open(users, 'r', encoding = "utf-8") as user:
		with open(hobbies, 'r', encoding = 'utf-8') as hobby:
			with open(users_hobbies, 'w+', encoding = 'utf-8') as user_hobby:
				for user_line, hobby_line in zip_longest(user, hobby, fillvalue = None):
					if user_line != None:
						user_line = user_line.replace("\n", "")
						recoding_line = f'{user_line}: {hobby_line}'
						user_hobby.write(recoding_line)
					else:
						return 1
				user_hobby.seek(0)
				print('⇓'*60)
				print('Returned value was written down in',users_hobbies, "file.")
				print('⇓'*60)
				answer = input("Do you want me to print the returned value in this \
terminal's session?\nThe values may be super huge. So it may take \
a while.\nPlease input yes or no only: ")
				if answer == 'yes':
					return user_hobby.read()
				else:
					print('Bye, dude!')

exit(write_names_hobbies(argv))
