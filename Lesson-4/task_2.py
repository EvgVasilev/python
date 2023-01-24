# var_1
def more_than(my_list):
    for i in range(1, len(my_list)):
        if my_list[i] > my_list[i - 1]:
            yield my_list[i]


li = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f'Итог v_1: {list(more_than(li))}')

# var_2
new_li = []
for i in range(len(li) - 1):
    x = li[i]
    i += 1
    y = li[i]
    if y > x:
        new_li.append(y)
print(f'Итог v_2: {new_li}')
