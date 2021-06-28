# 5. Подумайте, как можно сделать оптимизацию кода по памяти,
# по скорости.
# Представлен список чисел.
# Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка
# их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб».
# Потом подумайте об оптимизаци

import time

src = [2, 2, 2, 7, 23, 1, 44, 57, 44, 3, 2, 10, 7, 4, 11, 7]

# метод в лоб

# start = time.perf_counter()

result = [el for el in src if src.count(el) == 1]
print(result)

# finish = time.perf_counter()
# print(finish - start)

# оптимизация

# start = time.perf_counter()

results_set = set()
repeats = set()
for el in src:
    if el not in repeats:
      results_set.add(el)
    else:
      results_set.discard(el)
    repeats.add(el)

result_as_src_order = [el for el in src if el in results_set]
print(result_as_src_order)

# finish = time.perf_counter()
# print(finish - start)
