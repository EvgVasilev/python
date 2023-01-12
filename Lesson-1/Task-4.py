your_number = int(input('Введите целое положительное число: '))
max_num = 0
while your_number > 0:
    num = your_number % 10
    if num > max_num:
        max_num = num
    your_number = your_number // 10
print(f'Наибольшее число:{max_num}')
