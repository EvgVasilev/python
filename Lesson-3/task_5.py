def my_sum ():
    result = 0
    ex = False
    while ex == False:
        number = input('Введите числа разделяя их пробелом, либо Q для выхода - ').split()

        int_result = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                ex = True
                break
            else:
                int_result = int_result + int(number[el])
        result = result + int_result
        print(f'Сумма введенных чисел равна: {result}')
    print(f'Итоговая сумма чисел равна: {result}')


my_sum()