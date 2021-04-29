""" 4. Определить, какое число в массиве встречается чаще всего. """

from random import randint


my_list = [randint(1, 10) for i in range(20)]


def max_val_dict(any_list):
    my_dict = dict()
    max_val = 0
    for i in my_list:
        my_dict[i] = my_list.count(i)
        if my_dict[i] > max_val:
            max_val = my_dict[i]
    for key, val in my_dict.items():
        if val == max_val:
            return f'{key} : {val}'

print(my_list)
print(max_val_dict(my_list))


