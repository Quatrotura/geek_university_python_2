# Написать скрипт, который выводит статистику для заданной папки в виде словаря, 
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10), 
# а значения — общее количество файлов (в том числе и в подпапках), 
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#      {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }

# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import os

path = '/Users/SYakubov/desktop/programming/geekbrains/python/homeworks/Sergey_Yakubov_dz_7/some_data'


files_size_dict ={}

def qty_isNone(qty):
  """qty - значение по ключу.
  Проверка переменной qty. 
  Если None -  то ключ встречается впервые и значений нет и возвращается 0
  Если не None - то ключ встречался, у него уже есть значения, функция возвращает эти значения"""

  if qty == None:
    return 0
  else:
    return qty

def figures_count(size):
  """Считаем кол-во цифр в значении размера файла"""
  count = 0
  while size >= 1:
    size = size//10
    count += 1
  return count

def size_not_more(size, count):
  """Функция принимает размер файла и количество цифр в нем.
  Каталогизирует до ближайшего числа в соответствии с условиями задачи и возврашает его"""
  if size == 0:
    return 0
  elif size <= 10:
    return 10
  elif (size <= 10**count) and (size > 10**(count-1)):
    return 10**count
  else:
    return 10**(count-1)

def get_file_size(path):

  for file in os.scandir(path):
    # у меня макось, ОС создает скрытый системный файл .DSstore
    # решил, что он не должен участвовать в нашей спецоперации
    if file.name.startswith('.'):
      continue

    if os.path.isfile(file):
      file_size = file.stat().st_size

      #каталогизируем полученное значение размера файла
      key = size_not_more(file_size, figures_count(file_size))
      # записываем полученный ключ в словарь и записываем значение в qty
      qty = files_size_dict.setdefault(key)
      # проверяем и итерируем qty. Если qty == None, значит по этому ключу еще не было значений 
      qty = qty_isNone(qty) + 1
      files_size_dict[key] = qty

    else:
      get_file_size(os.path.join(path, file.name))

get_file_size(path)

print(files_size_dict)

