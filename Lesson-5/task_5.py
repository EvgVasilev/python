import random

int_file = open('int_file.txt', 'w', encoding='utf-8')

nums = (random.sample(range(100), 10))
print(" ".join(map(str, nums)), file=int_file)
int_file.close()

with open("int_file.txt", encoding='utf-8') as f_obj:
    result = 0
    items = f_obj.read().split(" ")
    for i in items:
        result = result + int(i)
    print(f"Сумма = {result}")
