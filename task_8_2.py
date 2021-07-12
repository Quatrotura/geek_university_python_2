# *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) 
# для получения информации вида: 
#(<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>), например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'

# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')

# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки? Можно ли для них уточнить регулярное выражение?

import requests
import re

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
line = '93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)'
response = requests.get(url)

REGEX_response = re.compile(r'([^\s-]+)\s\-\s\-\s*\[(.*?)\]\s*\"(\w+)\s*(\/\S*)\s*\S*\s*(\d{3})\s(\d*)\s', re.IGNORECASE)

parse_responce = REGEX_response.findall(response.text)

# проверочка
for el in parse_responce:
	print(el)

