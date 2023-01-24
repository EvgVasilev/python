import functools

my_list = [el for el in range(100, 1001) if el % 2 == 0]


def list_range(prev_el, el):
    return prev_el * el


print(functools.reduce(list_range, my_list))
