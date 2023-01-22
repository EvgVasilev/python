a = input('Введите делимое: ')
b = input('Введите делитель: ')


def my_div(a, b):
    '''Функция деления с проверкой вводимых значений'''
    while not a.isdigit() or not b.isdigit():
        print('Допускается ввод только чисел.')
        a = input('Введите делимое: ')
        b = input('Введите делитель: ')
    a = int(a)
    b = int(b)
    while True:
        if b == 0:
            print('Недопустимое значение делителя. Введите число отличное от "0"')
            b = input('Введите делитель: ')
            while not b.isdigit() or int(b) == 0:
                print('Введите любое число не равное 0')
                b = input('Введите делитель: ')
            b = int(b)
        elif a % b > 0:
            result = round(a / b, 5)
            break
        else:
            result = a // b
            break
    return print(f'Результат деления {a} на {b} равен {result}')


my_div(a, b)
