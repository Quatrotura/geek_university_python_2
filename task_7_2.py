# *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html


# Примечание: структуру файла config.yaml придумайте сами, 
# его можно создать в любом текстовом редакторе «руками» (не программно); 
# предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.

import os
import yaml

#загрузка конфига из ямла
with open('config.yaml','r') as f:
    config = yaml.safe_load(f)

def get_root(dictionary):
   """Функция берет ключ первого уровня и возвращает его.
   Это необходимо для того, чтобы в основной функции корень конфига не затирался.
   Это также помогает весь скрипт в целом сделать более универсальным, указав названия корня конфига
   только в ямле"""
   for key, value in dictionary.items():
      return key

def config_write(dictionary, path):
   """Создает конфигурацию проекта из словаря"""
   for key, value in dictionary.items():
      path += '/' + key
      path2 = ''
      try:     
         os.makedirs(os.path.join(path))
      except (FileExistsError) as e:
         print(f'Ошибка типа {e}:\nПапка {path} уже существует.\n')

      if isinstance(value, dict):
         config_write(value, path)
      else:            
         for value2 in value:
            if isinstance(value2, dict):
               config_write(value2, path)
            else:
               path2 = path + '/' + value2
               try:
                  with open(f'{os.path.join(path2)}', 'w', encoding = 'utf-8') as f:
                     pass
               except (FileExistsError) as e:
                  print(f'Файл {path2} уже существует.\n')

         path = os.getcwd() +'/' + get_root(config)

config_write(config, os.getcwd())

# проверочка:
root = 'my_project_2'

def get_txt(dir_name, ident):
   """проверочка: рекурсия для обхода cозданной директории
   печатает созданное дерево конфига"""
   ident += "|-"
   for item in os.listdir(dir_name):
      if os.path.isdir(os.path.join(dir_name,item)):
         print(ident, item)
         get_txt(os.path.join(dir_name, item), ident)
      else:
         print(ident, item)


get_txt(root, ident = "")

