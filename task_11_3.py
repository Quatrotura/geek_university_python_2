# Создать собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента. Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
import re
user_nums = []
user_input = ''

class OwnError(Exception):
    def __init___(self, msg):
        self.msg = msg

# вариант простой и самый очевидный и только целые числа:

while user_input != 'stop':
    user_input = input('Enter the number: ')
    
    try:
        if user_input.isnumeric() == False:
            raise OwnError('You shall input only numbers')  
    except OwnError as err:
        print(err)
    else:
        user_nums.append(user_input)
        
# если хотим иметь возможность вводить и integer и float, решил побаловаться с регулярками:
# def check_non_numeric(user_input):

#     regex = re.compile(r'[^\d\.]')
#     output = ''.join(regex.findall(user_input))
#     if output != '':
#         return False

# while user_input != 'stop':
#   user_input = input('Enter the number: ')
    
#   try:
#       if check_non_numeric(user_input) == False and user_input != 'stop' and user_input != '':
#           raise OwnError('You shall input only numbers')  
#   except OwnError as err:
#       print(err)
#   else:
#       if user_input.startswith('.'):
#           user_nums.append('0'+ user_input)
#       elif user_input != 'stop':
#           user_nums.append(user_input)

        
print(user_nums)