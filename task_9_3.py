class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': income, 'bonus': income * 0.75}


class Position(Worker):

    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)
        self.total_income = self._income['wage'] + self._income['bonus']

       
    def get_full_name(self):
        full_name = f'{self.name} {self.surname}'
        return full_name

    def get_total_income(self): 
        return self.total_income


me = Position('Sergey', 'Yakubov', 'Windowshopper', 1000)
print(me)
print(me.get_full_name())
print(me.get_total_income())