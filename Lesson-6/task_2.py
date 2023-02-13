class Road:
    def calculation(self, lenght, width, weight, depth):
        self._lenght = lenght
        self._width = width
        print(f'Результат расчета: {float(self._lenght * self._width * depth * weight / 1000)} т.')


a = Road()
a.calculation(int(input('Длина полотна: ')), int(input('Ширина полотна: ')), int(input('Вес 1 кв.м: ')),
              int(input('Толщина полотна: ')))
