# Реализовать класс Stationery (канцелярская принадлежность):
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:

	def __init__(self, title):
		self.title = title

	def draw(self):
		msg = 'Запуск отрисовки'
		return msg


class Pen(Stationery):

	def __init__(self, title):
		super().__init__(title)

	def draw(self):
		msg = 'Запуск отрисовки ручкой'
		return msg


class Pencil(Stationery):

	def __init__(self, title):
		super().__init__(title)

	def draw(self):
		msg = 'Запуск отрисовки карандашом'
		return msg


class Handle(Stationery):

	def __init__(self, title):
		super().__init__(title)

	def draw(self):
		msg = 'Запуск отрисовки маркером'
		return msg

obj_1 = Stationery('какой-то канцелярский предмет')
print(obj_1.draw())

obj_2 = Pen('ручка')
print(obj_2.draw())

obj_3 = Pencil('карандаш')
print(obj_3.draw())

obj_4 = Handle('маркер')
print(obj_4.draw())


