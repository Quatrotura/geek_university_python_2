# *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, 
# в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#     {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }

# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

import os

path = '/Users/SYakubov/desktop/programming/geekbrains/python/homeworks/Sergey_Yakubov_dz_7/some_data'

files_size_dict ={}

def qty_is_empty(qty):
  if len(qty) == 0:
    return [0,[]]
  else:
    return qty

def figures_count(size):
  count = 0
  while size >= 1:
    size = size//10
    count += 1
  return count

def size_not_more(size, count):

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
    if file.name.startswith('.'):
      continue

    if os.path.isfile(file):
      file_size = file.stat().st_size
      key = size_not_more(file_size, figures_count(file_size))
      qty = files_size_dict.setdefault(key,[])      
      qty = qty_is_empty(qty)
      qty[0] += 1
      files_size_dict[key] = qty
      files_size_dict[key][1].append(file.name)
    else:
      get_file_size(os.path.join(path, file.name))

get_file_size(path)

for key, value in files_size_dict.items():
  files_size_dict[key] = tuple(value)

print(files_size_dict)


