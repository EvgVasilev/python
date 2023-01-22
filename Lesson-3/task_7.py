# используем функцию из прошлого задания
from task_6 import int_func

words = input('Введите несколько слов, разделяя их пробелом: ').split()
print(*[int_func(w) for w in words])
