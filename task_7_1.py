# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp


# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); 
#как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; 
#можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

import os

root    = 'my_project'
subdirs = ['settings',
         'mainapp',
         'adminapp',
         'authapp',
         ]

for i in range(len(subdirs)):
   dir_path = os.path.join(root, subdirs[i])
   if not os.path.exists(dir_path):
      os.makedirs(dir_path)
   else:
      print(f'Папка {subdirs[i]} в директории {root} уже существует. Перезатирать не будем.')

