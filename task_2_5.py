# 5. Создать список, содержащий цены на товары (10–20 товаров),

price_list = [57.8, 46.51, 97, 100.34, 73.12, 674.09, 4239.92, 93, 18475.76, 458093.02]

# * Вывести на экран эти цены через запятую в одну строку, 
# цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). 
# Подумать, как из цены получить рубли и копейки, как добавить нули, 
# если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).


rouble  = 0
kopeika = 0
line    = ''
ind = 0

while ind < len(price_list):
	kopeika = round(price_list[ind] % 1 * 100)
	rouble = int(price_list[ind] // 1)
	# kopeika = (price_list[ind] - price_list[ind] // 1) * 100
	# print(price_list[ind], rouble, kopeika)
	print(f'{rouble} руб {kopeika:02d} коп, ', end = '')
	ind += 1

## * Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
print('\n')
print('+'*50)

print(id(price_list))
price_list.sort()
print(price_list)
print(id(price_list))

# * Создать новый список, содержащий те же цены, но отсортированные по убыванию.
print('+'*50)
price_list_rev = sorted(price_list, reverse = True)
print(price_list_rev)
print(id(price_list_rev))

# * Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

print(price_list[-5:])