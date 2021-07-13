class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        msg = f'{self.name.title()} поехала!'
        return msg

    def stop(self):
        msg = f'{self.name.title()} остановилась'
        return msg

    def turn(self, direction):
        msg = f'{self.name.title()} повернула {direction.lower()}'
        return msg

    def show_speed(self):
        msg = f'Текущая скорость {self.name.title()}: {self.speed} км/ч'
        return msg


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):

        if self.speed > 60:
            print(f'Лимит скорости превышен на {self.speed - 60} км/ч')
            return self.speed
        else:
            print(f'Текущая скорость {self.name.title()}: {self.speed} км/ч')
            return self.speed


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Лимит скорости превышен на {self.speed - 40} км/ч')
            return self.speed
        else:
            print(f'Текущая скорость {self.name.title()}: {self.speed} км/ч')
            return self.speed


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


audi = Car(70, 'black', 'audi a6', True)
print(audi.go())
print(audi.stop())
print(audi.turn('налево'))
print(audi.show_speed())
print(audi.is_police)

print('%' * 100, end = '\n\n')

lada = TownCar(80, 'white', 'lada vesta', False)
print(lada.go())
print(lada.stop())
print(lada.turn('взад'))
print(lada.show_speed())
print(lada.is_police)

print('%' * 100, end = '\n\n')

uaz = WorkCar(41, 'blue', 'uaz patriot', False)

print(uaz.go())
print(uaz.stop())
print(uaz.turn('левее'))
print(uaz.show_speed())
print(uaz.is_police)
