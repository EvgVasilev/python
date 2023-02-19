class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if self.b + other.b < 0:
            return f'Сумма равна: {self.a + other.a} - {abs(self.b + other.b)} * i'
        return f'Сумма равна: {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        if self.b * other.a < 0:
            return f'Произведение равно: {self.a * other.a - (self.b * other.b)} - {abs(self.b * other.a)} * i'
        return f'Произведение равно: {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'


number_1 = ComplexNumber(7, -18)
number_2 = ComplexNumber(-12, 9)
print(number_1 + number_2)
print(number_1 * number_2)

number_1 = ComplexNumber(-5, -3)
number_2 = ComplexNumber(15, 3)
print(number_1 + number_2)
print(number_1 * number_2)
