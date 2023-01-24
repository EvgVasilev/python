from itertools import cycle
for el in range(3,11):
    print(el)


i = 0
for el in cycle('Hello world '):
    if i > 20:
        break
    print(el)
    i += 1




