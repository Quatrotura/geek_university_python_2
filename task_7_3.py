# Создать структуру файлов и папок, как написано в задании 2 
# (при помощи скрипта или «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#    |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html


# Примечание: исходные файлы необходимо оставить; 
# обратите внимание, что html-файлы расположены в родительских папках 
# (они играют роль пространств имён); 
# предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.


import os
from shutil import copy2, copy, SameFileError

dest_dir_name = 'templates'
dir_path = '/Users/SYakubov/desktop/programming/geekbrains/python/homeworks/Sergey_Yakubov_dz_7/my_project_2'
dest_dir_path = '/Users/SYakubov/desktop/programming/geekbrains/python/homeworks/Sergey_Yakubov_dz_7/my_project_2/' + dest_dir_name

# первая версия кода без try-exception

# def get_templates(dir_path):

#    for item in os.listdir(dir_path):
#       item_path = os.path.join(dir_path, item)

#       if os.path.isdir(item_path):
#          get_templates(item_path)
#       else:
#          if dest_dir_name in item_path:
#             if not os.path.basename(item_path).startswith('.'):
#                file_parent_dir = os.path.dirname(item_path).split('/')[-1]
#                file_name = os.path.basename(item_path) 
#                new_file_path = os.path.join(dest_dir_path, file_parent_dir)
#                if not os.path.exists(dest_dir_path):
#                   os.makedirs(dest_dir_path)
#                if not os.path.exists(new_file_path):
#                   os.makedirs(new_file_path)
#                if not file_name.startswith('.'):
#                   copy(item_path, new_file_path)
#                   print(file_name, 'copied to', new_file_path)

def get_templates(dir_path):

   for item in os.listdir(dir_path):
      item_path = os.path.join(dir_path, item)

      if os.path.isdir(item_path):
         get_templates(item_path)
      else:
         if dest_dir_name in item_path:
            if not os.path.basename(item_path).startswith('.'):
               file_parent_dir = os.path.dirname(item_path).split('/')[-1]
               file_name = os.path.basename(item_path) 
               new_file_path = os.path.join(dest_dir_path, file_parent_dir)

               try:
                  os.makedirs(dest_dir_path)
               except (FileExistsError) as e:
                  pass
               try:
                  os.makedirs(new_file_path)
               except (FileExistsError) as e:
                  pass 


               if not file_name.startswith('.'):
                  try:
                     copy(item_path, new_file_path)
                     print(file_name, 'copied to', new_file_path)
                  except SameFileError as e:
                     pass



get_templates(dir_path)



