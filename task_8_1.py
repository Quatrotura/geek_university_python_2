# Написать функцию email_parse(<email_address>), 
# которая при помощи регулярного выражения извлекает имя пользователя и 
# почтовый домен из email адреса и возвращает их в виде словаря. 
# Если адрес не валиден, выбросить исключение ValueError. Пример:

# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru

# def email_parse(email):

import re

email_address = 'someone@geekbrains.ru'
msg = f'ValueError: wrong email: {email_address}'

def email_parse(email_address):

    REGEX_EMAIL = re.compile(r'(?P<username>[a-zA-Z0-9\.\-_]+)@(?P<domain>[a-z0-9]+[\.][a-z]+)')
    try:
        assert REGEX_EMAIL.match(email_address)
        print(*map(lambda x: x.groupdict(), REGEX_EMAIL.finditer(email_address)))
    except AssertionError:
        raise ValueError(msg)

email_parse(email_address)
