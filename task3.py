""" 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы. """

from random import randint


my_list = [randint(1, 100) for i in range(4)]

max_el = 0
min_el = 100

for i in my_list:
    if i > max_el:
        max_el = i
    if i < min_el:
        min_el = i

inx_max_el = my_list.index(max_el)
inx_min_el = my_list.index(min_el)
print(f'max = {max_el}, min = {min_el}')
print(my_list)
my_list[inx_max_el], my_list[inx_min_el] = min_el, max_el

print(my_list)

