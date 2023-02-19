class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    all_stuff = []

    def __init__(self, device, name, price, quantity):
        self.device = device
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items = {'Модель': self.name, 'Цена': self.price, 'Количество': self.quantity}


class Equipment(Warehouse):
    def add_to_wh(self, device):
        try:
            name = input('Введите название модели: ')
            price = input('Введите цену: ')
            if not price.isnumeric():
                raise MyException('Цену необходимо указать числом.')
            quantity = input('Введите количество: ')
            if not quantity.isnumeric():
                raise MyException('Количество необходимо указать числом.')
            item = {'Тип': device, 'Модель': name, 'Цена': price, 'Количество': quantity}
            self.items.update(item)
            print(self.items)
            self.all_stuff.append(self.items)

        except MyException as err:
            print(err)


class Printer(Equipment):
    pass


class Scanner(Equipment):
    pass


class Xerox(Equipment):
    pass


printer = Printer('example', 'example', 0, 0)
scanner = Scanner('example', 'example', 0, 0)
xerox = Xerox('example', 'example', 0, 0)

while True:
    add_item = input('Ввести данные для принтера - p, сканера - s, ксерокса - x, для выхода - q: ')

    if add_item in ('p', 'P'):
        printer.add_to_wh(device='Принтер')
    elif add_item in ('s', 'S'):
        scanner.add_to_wh(device='Сканер')
    elif add_item in ('x', 'X'):
        xerox.add_to_wh(device='Ксерокс')
    elif add_item in ('q', 'Q'):
        break
    else:
        print('Ошибка! Повторите ввод.')

print(Warehouse.all_stuff)
