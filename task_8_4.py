# Написать декоратор с аргументом-функцией (callback), 
# позволяющий валидировать входные значения функции 
# и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...

# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3

# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?

from functools import wraps

def get_type(func):

    @wraps(func)
    def wrapper(*args):
        cube = func(*args)
        for el in args:
            print(f'{func.__name__}({el}: {type(el)})', end = ', ')            
        print(f'\nReturning result {cube}, type is {type(cube)}')
        return cube

    return wrapper

def val_checker(isNatural):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            x = args[0]
            if isNatural(x):
                result = func(*args)
                return result
            else:
                num = ','.join(map(str, args))
                msg = f'wrong value {num}'
                raise ValueError(msg)

        return wrapper
    return _val_checker  

@val_checker(lambda x: x > 0)
@get_type
def calc_cube(x):
    return x ** 3


check = calc_cube(5)
print(calc_cube)
