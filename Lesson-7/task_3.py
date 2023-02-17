class Cell:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return f'Сумма клеток = ({self.n + other.n})'

    def __sub__(self, other):
        result = self.n - other.n
        if result > 0:
            return f'Разность клеток = ({result})'
        else:
            return f'Операция невозможна, результат меньше 0'

    def __mul__(self, other):
        return f'Умножение клеток =  ({self.n * other.n})'

    def __truediv__(self, other):
        return f'Деление клеток =  ({round(self.n / other.n)})'

    def make_order(self, order):
        result = self.n % order
        return ('*' * order + '\\n ') * int(self.n / order) + '*' * result


cell1 = Cell(30)
cell2 = Cell(25)
cell3 = Cell(10)
cell4 = Cell(15)

print(f'Сложение:\n {cell1 + cell2}\n')
print(f'Вычитание:\n {cell2 - cell1}\n {cell4 - cell3}\n')
print(f'Умножение:\n {cell2 * cell1}\n')
print(f'Деление:\n {cell1 / cell2}\n')
print(f'Организация ячеек по рядам:\n {cell1.make_order(3)};\n {cell2.make_order(4)}')

