class MyException(Exception):

    def __str__(self):
        return f"Недопустимое значение 0"


i = True
while i is True:
    try:
        num = int(input('Введите делитель: '))
        if num == 0:
            raise MyException
        print(100 / num)
        print('Выход')
        i = False
    except MyException as result:
        print(result)
