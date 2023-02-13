class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Ручка'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Карандаш'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Маркер'


item = Pencil('Koh-i-noor')
print(f'{item.title}, {item.draw()}')
item = Pen('Parker')
print(f'{item.title}, {item.draw()}')
item = Handle('ErichKrause')
print(f'{item.title}, {item.draw()}')
