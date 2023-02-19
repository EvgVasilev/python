import datetime


class Date:
    day_month_year = '18_02_2023'
    day = 0
    month = 0
    year = 0

    @classmethod
    def date2num(cls):
        cls.day = int(cls.day_month_year.split('_')[0])
        cls.month = int(cls.day_month_year.split('_')[1])
        cls.year = int(cls.day_month_year.split('_')[2])
        return cls.day, cls.month, cls.year

    @staticmethod
    def date_valid(day_month_year):
        day, month, year = map(int, day_month_year.split('_'))
        try:
            datetime.datetime(year, month, day)
        except ValueError:
            print(f'{day_month_year} неверная дата')


print(Date.date2num())
print(Date.day)
print(Date.month)
print(Date.year)
Date.date_valid('29_02_2023')