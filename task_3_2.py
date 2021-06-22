# 2. *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): 
# реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

numbers_dict = {'zero':  'ноль',
				'one':   'один',
				'two': 	 'два',
				'three': 'три',
				'four':  'четыре',
				'five':  'пять',
				'six': 	 'шесть',
				'seven': 'семь',
				'eight': 'восемь',
				'nine':  'девять',
				'ten': 	 'десять',
				}

def num_translate(el_num):

	if el_num[0].isupper() == False:
		return numbers_dict.get(el_num)
	return numbers_dict.get(el_num.lower(),'None').title()

# print(num_translate('Eleven'))

# for i in numbers_dict:
# 	print(i.title(), num_translate(i.title()))
