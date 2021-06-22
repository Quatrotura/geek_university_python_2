# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# 3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача намного серьёзнее, чем может сначала показаться.

# Женя, я не понимаю в чем отличие этой задачи от второй. 
# В реализации второй задачи я все сделал не создавая новый список, то есть inplace т.к. такое было условие второй задачи
# Ниже реализация второй задачи без модификации  списка вообще

msg = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# в "05" часов "17" минут температура воздуха была "+05" градусов

i = 0
line = ''
line_2=''
plus = ''

while i < len(msg):
	if msg[i].isalpha() == False:
		if msg[i][0] == '+':
			plus = "+"
		line = f'{line}"{plus}{int(msg[i]):02d}" '
		
	else:
		line = f'{line}{msg[i]} '
	plus = ''
	i += 1
	
print(line)