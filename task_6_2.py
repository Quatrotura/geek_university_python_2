# *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

from collections import Counter

ip_list = []
logs = []

with open('nginx_logs.txt', 'r', encoding = 'utf-8') as f:
	logs = [line.split(' ') for line in f]

ip_list = [line[0] for line in logs]
print(Counter(ip_list).most_common(1))
