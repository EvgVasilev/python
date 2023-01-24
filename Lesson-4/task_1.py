from sys import argv

script_name, hours, rate, award = argv
print('Расчет заработной платы: ')
print('Выработка часов: ', float(hours))
print('Ставка: ', float(rate))
print('Премия: ', float(award))

cash_month = float(hours) * float(rate) + float(award)
print(f'Расчетная заработная плата {cash_month}')
