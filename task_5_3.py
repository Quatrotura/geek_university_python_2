# Есть два списка:
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей', 
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]

# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')

# Количество генерируемых кортежей не должно быть больше длины списка tutors. 
# Если в списке klasses меньше элементов, чем в списке tutors, 
# необходимо вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)

# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких ситуациях генератор даст эффект. 

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Давид', 'Марк'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

from sys import getsizeof
from itertools import zip_longest

# решение через создание функции, использование йилда
def tutor_klass_gen(tutors, klasses):

    for tutor, klass in zip_longest(tutors, klasses, fillvalue = 'None'):
        yield tutor, klass

g = tutor_klass_gen(tutors, klasses)

# проверочка:

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(type(g))

# решение без йелда

gen = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses, fillvalue = "None"))

# проверочка:

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(type(gen))

# что характерно

print(getsizeof(g), getsizeof(gen))



