# Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый — с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать
# их тип к типу «Число». Второй — с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

from datetime import datetime

 

class Date:

    def __init__(self, date: str):
        self.date = date

    # Не очень понятна задача. Если под "число" имеется в # виду тип datetime, то код ниже. Если тип int, то см. след метод
    @classmethod
    def get_date(cls, date: str):
        cls.day, cls.month, cls.year = map(int, date.split('-'))
        date = datetime(day=cls.day, month=cls.month, year=cls.year)
        return date

    @classmethod
    def get_int(cls, date: str):
        cls.day, cls.month, cls.year = map(int, date.split('-'))

        print(f'\n"get_int" classmethod\nDay: {cls.day} {type(cls.day)}\n\
Month: {cls.month} {type(cls.day)}\nYear: {cls.year} {type(cls.day)}\n')

        return map(int, date.split('-'))

    @staticmethod
    def validate_args(date):
        day, month, year = Date.get_int(date)

        if day >= 1 and day <= 31:
            print('Day value checked: ok')
        else:
            print('Day value checked: not ok.\
The value must be within 1-31 range.')

        if month >= 1 and month <= 12:
            print('Month value checked: ok')
        else:
            print('Month value checked: not ok.\
The value must be within 1-12 range.')

        if year != 0:
            print('Year value checked: ok')
        else:
            print('Year value checked: not ok.\
The value must not be equal to zero')


print(Date.get_date('10-05-2021'))
Date.get_int('11-05-2022')
Date.validate_args('32-12-2021')