import json

firm_list = open('firm_list.txt', 'r', encoding='utf-8')
firm_dict = {}
average_profit_dict = {}
average_profit = 0

for line in firm_list:
    firm = line.split()
    profit = int(firm[2]) - int(firm[3])
    firm_dict[firm[0]] = profit
    if profit >= 0:
        average_profit += profit

average_profit_dict['average_profit'] = average_profit
result = [firm_dict, average_profit_dict]
firm_list.close()

with open('firm_dict.json', 'w') as out_file:
    json.dump(result, out_file)
out_file.close()
