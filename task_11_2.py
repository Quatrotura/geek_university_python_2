# Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
# Проверить его работу на данных, вводимых пользователем. 
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class CustomizedErrorClass(Exception):
	def __init__(self, error_msg):
		self.error_msg = error_msg

def division():

	a = int(input('Введите делимое: '))
	b = int(input('Введите делитель: '))

	try:
		if b == 0:
			raise CustomizedErrorClass('Делить на ноль нельзя!')

		result = a / b

	except CustomizedErrorClass as msg:
		print(msg)
		division()

	else:
		print(result)


division()






