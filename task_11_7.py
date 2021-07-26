# Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число». 
# Реализовать перегрузку методов сложения и умножения комплексных чисел. Проверить работу проекта. 
# Для этого создать экземпляры класса (комплексные числа), выполнить сложение и умножение созданных экземпляров. 
# Проверить корректность полученного результата.

class ComplexNumber:
 
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
    def __add__(self, other):
        return complex(self.a, self.b) + complex(other.a, other.b)

 
    def __mul__(self, other):
        return complex(self.a, self.b) * complex(other.a, other.b)

 
num1 = ComplexNumber(2, 3)
num2 = ComplexNumber(3, 4)
 
print(num1 + num2)
print(num1 * num2)
