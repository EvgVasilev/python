usr_str = input('Введите несколько, слов раздяляя их пробелом: ').split()
for count, el in enumerate(usr_str,1):
    print(f'{count} - {el[:10]}')
