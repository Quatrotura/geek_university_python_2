
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]

import requests

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
tupled_list_logs = []
response = requests.get(url)

with open('nginx_logs.txt', 'w', encoding = "utf-8") as f:
	f.write(response.text)

with open('nginx_logs.txt', 'r', encoding = 'utf-8') as f:
	logs = f.read().splitlines()


logs = [logs[line].split(' ') for line in range(len(logs))]
tupled_list_logs = [(line[0], line[5].replace('"', ''), line[6]) for line in logs]

# проверочка
print(tupled_list_logs)
