class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


def only_num():
    num_list = []
    while True:
        nums = input(f'Введите число, или stop для выхода: ')
        if nums == 'stop':
            break
        try:
            if not nums.isnumeric():
                raise MyException('Введено не число.')
            num_list.append(nums)
        except MyException as err:
            print(err)
    print(f'Вы ввели следующие числа:')
    print(*num_list)


only_num()
