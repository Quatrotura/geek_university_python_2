# Реализовать проект расчёта суммарного расхода ткани на производство одежды. 
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. 
# К типам одежды в этом проекте относятся пальто и костюм. 
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
# Это могут быть обычные числа: V и H соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: 
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). 
# Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. 
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def get_fabric_consumption(self):
        pass


class Coat(Clothes):

    def __init__(self, v_size):
        self.v_size = v_size

    @property
    def get_fabric_consumption(self):
        return self.v_size / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, h_height):
        self.h_height = h_height

    @property
    def get_fabric_consumption(self):
        return self.h_height * 2 + 0.3


a = Coat(56)
print(a.get_fabric_consumption)

b = Suit(185)
print(b.get_fabric_consumption)

