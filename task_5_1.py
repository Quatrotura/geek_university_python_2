# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield

def odd_numbers_gen(max_num):
    for odd_num in range(1, max_num + 1, 2):
        yield odd_num


g = odd_numbers_gen(15)

# проверочка:

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
