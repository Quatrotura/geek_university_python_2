# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...

# @type_logger
# def calc_cube(x):
#    return x ** 3

# >>> a = calc_cube(5)
# 5: <class 'int'>

# Примечание: если аргументов несколько - выводить данные о каждом через запятую; 
# можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов? 
# Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)


from functools import wraps

def get_type(func):

   @wraps(func)
   def wrapper(*args, **kwargs):

      cube = func(*args, **kwargs)
      arguments = list(args)
      arguments.extend([val for val in kwargs.values()])
      for el in arguments:
         print(f'{func.__name__}({el}: {type(el)})', end = ', ')      
      
      print(f'\nReturning result {cube}, type is {type(cube)}')
      return cube

   return wrapper

@get_type
def calc_cube_plus(num, power, plus, **kwargs):
   kwargi = kwargs
   return (num ** power + plus) * kwargi['x'] - kwargi['y']

check = calc_cube_plus(5, 3, 0, x = 1.0, y = 1)

print(calc_cube_plus)
