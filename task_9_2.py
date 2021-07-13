# Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, 
# необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта 
# для покрытия одного кв. метра дороги асфальтом, 
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
 
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road():

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_volume(self, weight_per_1cm_thick, thickness):
        self.weight_per_1cm_thick = weight_per_1cm_thick
        self.thickness = thickness
        volume = self._length * self._width *self.weight_per_1cm_thick * self.thickness // 1000
        print(volume)
        return volume


check = Road(5000, 20)
check.get_volume(25, 5)