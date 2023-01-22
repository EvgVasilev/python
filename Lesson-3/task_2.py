name = input('Имя: ')
s_name = input('Фамилия: ')
b_year = input('Год рождения: ')
from_city = input('Город проживания: ')
e_mail = input('Электронная почта: ')
phone = input('Телефон: ')


def user_info(name, s_name, b_year, from_city, e_mail, phone):
    return name, s_name, b_year, from_city, e_mail, phone


print(user_info(name, s_name, b_year, from_city, e_mail, phone))