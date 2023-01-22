a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))


def my_func(a, b, c):
    int_list = [a, b, c]
    int_list.sort()
    int_list.reverse()
    return sum(int_list[0:2])


print(my_func(a, b, c))
