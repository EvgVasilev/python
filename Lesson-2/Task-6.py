goods = []
number = 0
while True:
    choice_goods = input("Желаете добавить новый товар? д/н: ")
    if choice_goods == 'д':
        prod = input('Введите название: ')
        cost = input('Введите цену: ')
        count = input('Введите количество: ')
        unit = input('Введите единицу измерения: ')
        number += 1
        goods.append(tuple([number, {'Название': prod, 'Цена': cost, 'Количество': count, 'Ед.Изм.': unit}]))
        print(goods)
    elif choice_goods == 'н':
        print('Ввод товаров закончен.')
        break
    else:
        print('Недопустимое значение.')
        continue

if not goods:
    print('Нет введенных товаров.')

else:
    print('Список введенных товаров:')
    for el in goods:
        print(el)
    while True:
        choice_analitics = input('Вывести аналитику? д/н: ')
        if choice_analitics == 'д':
            print('Аналитика')
            analitics = {}
            prod_set = set()
            costs_set = set()
            counts_set = set()
            units_set = set()
            for good in goods:
                prod_set.add(good[1]['Название'])
                costs_set.add(good[1]['Цена'])
                counts_set.add(good[1]['Количество'])
                units_set.add(good[1]['Ед.Изм.'])
            goods_analatic = {'Название': prod_set, 'Цена': costs_set, 'Количество': counts_set, 'Ед.Изм.': units_set}
            print(goods_analatic)
            break
        elif choice_analitics == 'н':
            print('Программа завершена.')
            break
        else:
            print('Введено неверное значение. д/н?')
            continue