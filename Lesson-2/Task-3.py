seasons_dict = {'Зима': (1, 2, 12),
                'Весна': (3, 4, 5),
                'Лето': (6, 7, 8),
                'Осень': (9, 10, 11)}
seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']

month = int(input('Введите номер месяца: '))
if month >= 1 and month <= 12:
    for key in seasons_dict.keys():
        if month in seasons_dict[key]:
            print(key)

    if month == 1 or month == 12 or month == 2:
        print(seasons_list[0])
    elif month >= 3 and month <= 5:
        print(seasons_list[1])
    elif month >= 6 and month <= 8:
        print(seasons_list[2])
    elif month >= 9 and month <= 11:
        print(seasons_list[3])
else:
    print('Месяца с таким номером не существует.')