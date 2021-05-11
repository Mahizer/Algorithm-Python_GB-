""" 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]."""

from itertools import zip_longest
from collections import deque


my_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
          '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
          'C': 12, 'D': 13, 'E': 14, 'F': 15}

first_num = [i for i in input('Введите любой набор чисел и букв (123456789ABCDEF): ')]
second_num = [i for i in input('Введите любой набор чисел и букв (123456789ABCDEF): ')]
sum1 = 0
sum2 = 0
index = 0


def my_hex(sum_, any_dict):
    new_lst = deque()
    idx = 0
    while sum_ > 10:
        new_lst.appendleft(sum_ % 16)
        sum_ //= 16
    else:
        new_lst.appendleft(sum_)
    for i in new_lst:
        for key, value in any_dict.items():
            if value == i:
                print(key, end='')
                idx += 1
    print()

first_num.reverse(), second_num.reverse()

for val, val2 in zip_longest(first_num, second_num):
    sum1 += my_num[val] * (16 ** index)
    if val2 is not None:
        sum2 += my_num[val2] * (16 ** index)
    index += 1

total_sum = sum1 + sum2
multi = sum1 * sum2


my_hex(total_sum, my_num)
my_hex(multi, my_num)
