""" 7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться."""

from random import randint

my_list = [randint(-10, 25) for i in range(12)]


def two_min_num(any_list):
    min_1, min_2 = my_list[0], my_list[0]
    for el in my_list:
        if el < min_1:
            min_1 = el
    for el2 in my_list:
        if min_1 < el2 < min_2:
            min_2 = el2
    return min_1, min_2

print(my_list)
print(two_min_num(my_list))
