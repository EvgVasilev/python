def my_func(x, y):
    return x ** y


print(my_func(2, -3))


def my_func1(a, b):
    b = abs(b)
    num = 1
    for i in range(0, b):
        num /= a
    return num


print(my_func1(2, -3))
