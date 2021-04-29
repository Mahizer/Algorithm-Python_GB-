""" 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать. """

from random import randint

my_list = [randint(-10, 25) for i in range(12)]
max_el, min_el = my_list[0], my_list[0]
inx_max = my_list.index(max_el)
inx_min = my_list.index(min_el)
sum_num = 0

for el in my_list:
    if el > max_el:
        max_el = el
        inx_max = my_list.index(max_el)
    elif el < min_el:
        min_el = el
        inx_min = my_list.index(min_el)

if inx_max == (inx_min + 1 or inx_min - 1) or inx_min == (inx_max + 1 or inx_max - 1):
    sum_num = 0
elif inx_max > inx_min:
    for el in my_list[inx_min+1:inx_max]:
        sum_num += el
else:
    for el in my_list[inx_min:inx_max:-1]:
        sum_num += el

print(my_list)
print(f'{max_el = }, {min_el = }')
print(sum_num)

