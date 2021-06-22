# 4. Подумать, какое условие записать, чтобы выявить числа среди элементов списка? 
# Как модифицировать это условие для чисел со знаком?

# 4.1. если числа - integer, float

mix = [1, 2, 3, 4, 5, 6,'something', 23, 'hello', 12, "what", -3, 3.4, 'wow', -14]

print(mix)

numbers = []

for el in mix[:]:
	if isinstance(el, int) == True or isinstance(el, float) == True:
		numbers.append(mix.pop(mix.index(el)))

print(mix)
print(numbers)
print("-"*30,'end',"-"*32,'\n')

# 4.1.2. если числа - строчные значения

mix = ["1", "2", "3", "4", "5", "6",'something', "23", 'hello', "12", "what", "-3", "3.4", 'wow', "-14"]
numbers = []

print(mix)

for el in mix[:]:
	if el.isalpha() == False:
		numbers.append(mix.pop(mix.index(el)))

print(mix)
print(numbers)
print("-"*30,'end',"-"*32,'\n')

# 4.2. Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

# Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!' 
# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. 
# Можно ли при этом не создавать новый список?

people = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
print(id(people))

name = ''
ind = 0
for el in people:
	people[people.index(el)] = el.split(' ')
	# print(people)
	name = ''.join(people[ind][-1:])
	# print(name)
	ind +=1
	print('Привет,', name.title())
	# print(type(name))

print(id(people))

# # for el in people:
# # 	people[people.index(el)] = el[::-1]
# 	# print(''.join(reversed(el)))
