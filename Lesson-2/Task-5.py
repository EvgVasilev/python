my_list = [7, 5, 3, 3, 2]
num = int(input("Введите натуральное число: "))
my_list.append(num)
my_list.sort()
my_list.reverse()
print(f"Текущий рейтинг: {my_list}")