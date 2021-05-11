""" 1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего."""

import collections


amt_company = int(input('Введите кол-во предприятий: '))
company_name = []
company_data = collections.defaultdict(list)
profit = 0
avg = 0
less_avg = []
more_avg = []
Q = 4  # кварталы

for i in range(amt_company):
    company_name.append(input('Введите наименование предприятия: '))
    for n in range(1, Q + 1):
        print(f'Прибыл за {n} квартал: ', end=' ')
        profit += int(input())
    company_data[company_name[i]].append('%.2f' % profit)
    avg += float('%.2f' % (profit / amt_company))
    profit = 0

for items, val in company_data.items():
    print(company_data[items][0])
    if float(company_data[items][0]) < avg:
        less_avg.append(items)
    else:
        more_avg.append(items)

print('Предприятия у кот.доход больше среднего : ', {*more_avg})
print('Предприятия у кот.доход меньше среднего : ', {*less_avg})
