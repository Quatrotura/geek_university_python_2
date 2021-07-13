# Создать класс TrafficLight (светофор):
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
 
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
import time

class TrafficLight:

	__color = []

	def running(self, *args):
		color_seq = ('red', 'yellow', 'green')
		sleep_args = (7, 2, 5)

		if len(args) == len(color_seq):

			for i in range(len(args)):
				if color_seq[i] != args[i]:
					msg = "Неверный порядок цветов светофора"
					print(msg)
					return False

			i = 0
			for el in args:				
				self.el = el
				TrafficLight().__color.append(self.el)
				print(f'{el} will last {sleep_args[i]} seconds')
				time.sleep(sleep_args[i])
				i += 1

			# print(*TrafficLight().__color)
			return TrafficLight().__color
		
		else:
			msg = 'У нашего светофора только три цвета'
			print(msg)
			return False



a = TrafficLight()
a.running('red','yellow', 'green')







