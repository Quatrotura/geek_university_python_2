# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), 
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.


# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц). 
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно. 
# Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.

# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), 
# который должен принимать данные (список списков) для формирования матрицы.

matrixed_list_1 = [[2, 3, 8],       [5, 2],    [0, 4]]
matrixed_list_2 = [[3, 2, 1, 5],    [2, 4, 7], [7, 3]]
matrixed_list_3 = [[4, 1],          [1, 3],    [1, 2]]

class Matrix():

    def __init__(self, m_list):
        self.m_list = m_list
        matrix_line = ''

    def __str__(self):
        matrix_line = ''
        for row in self.m_list:
            for el in row:
                matrix_line += f"{el}  "
            matrix_line += '\n'
        return matrix_line

    def __add__(self, other):
        n_list = []
        matrix_line = ''
        diff = 0
        for i in range(len(self.m_list)):
            n_list.append([])

            # comparing matrices length, var 'diff' is length difference, 
            #append zeros to shorter matrices to avoid index out of range mistake

            if len(self.m_list[i]) < len(other.m_list[i]):
                diff = len(other.m_list[i]) - len(self.m_list[i])
                for el in range(diff):
                    x = 0
                    self.m_list[i].append(x)

            elif len(self.m_list[i]) > len(other.m_list[i]):
                diff = len(self.m_list[i]) - len(other.m_list[i])
                for el in range(diff):
                    x = 0
                    other.m_list[i].append(x)
            # вот эта часть как у гуманитария заняла у меня около 1го часа :-))
            for i2 in range(len(self.m_list[i])):
                n_list[i].append(self.m_list[i][i2] + other.m_list[i][i2])

        return Matrix(n_list)


m_list_1 = Matrix(matrixed_list_1)
m_list_2 = Matrix(matrixed_list_2)
m_list_3 = Matrix(matrixed_list_3)

print(str(m_list_1))
print(str(m_list_2))

print(m_list_1 + m_list_2 + m_list_3)
