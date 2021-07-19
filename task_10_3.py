# Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка». 
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). 
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), 
# вычитание (__sub__()), умножение (__mul__()), деление (__floordiv____truediv__()). 
# Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и 
# округление до целого числа деления клеток соответственно.

# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Этот метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. 
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. В этом случае метод make_order() вернёт строку: *****\n*****\n**.
# Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. Тогда метод make_order() вернёт строку: *****\n*****\n*****


class OrganicCell:

    def __init__(self, cells_qty):
        if isinstance(cells_qty, int):
            self.cells_qty = cells_qty
        else:
            print('The cells_qty must be of integer type only. Pls try again.')
            exit(1)

    def __add__(self, other):
        return self.cells_qty + other.cells_qty

    def __sub__(self, other):
        if self.cells_qty - other.cells_qty > 0:
            return self.cells_qty - other.cells_qty
        else:
            msg = 'This operation does not make any sense.'
            return msg

    def __mul__(self, other):
        return self.cells_qty * other.cells_qty

    def __floordiv__(self, other):
        return self.cells_qty // other.cells_qty

    def __truediv__(self, other):
        return self. cells_qty // other.cells_qty

    def make_order(self, cells_in_row):
        self.cells_in_row = cells_in_row
        rows_qty = self.cells_qty // cells_in_row
        last_row_cells = self.cells_qty % cells_in_row

        for i in range(rows_qty):
          print('*' * cells_in_row)

        if last_row_cells:
            print('*' * last_row_cells)

    
    
a = OrganicCell(11)
b = OrganicCell(16)
print(a-b)
b.make_order(5)
