# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, 
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. 
# Например:
# >>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"], 
#     "М": ["Мария"], "П": ["Петр"]
# }
# Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?

def thesaurus(*args):
    names_dict = {}
    names_list = list(args)   
    #сортируем список имен, чтобы сразу отсортировать ключи в словаре
    for i in sorted(names_list):
        names_dict.setdefault(i[0],[]).append(i)
    return names_dict

print(thesaurus('Сергей', "Иван", "Мария", "Петр", "Илья", 'Светлана', 'Андрей', "Марина", 'Иосиф', "Педро", 'Алексей'))

# print(dir(dict))
