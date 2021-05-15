""" 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы."""

from random import uniform
from operator import lt

lst = ['%.2f' % (uniform(0, 49)) for _ in range(12)]
print(lst)


def merge_sort(list_):
    if len(list_) <= 1:
        return list_

    mid = len(list_) // 2
    left = merge_sort(list_[:mid])
    right = merge_sort(list_[mid:])
    result = []
    left_i = right_i = 0
    while left_i < len(left) and right_i < len(right):
        if left[left_i] < right[right_i]:
            result.append(left[left_i])
            left_i += 1
        else:
            result.append(right[right_i])
            right_i += 1
    while left_i < len(left):
        result.append(left[left_i])
        left_i += 1
    while right_i < len(right):
        result.append(right[right_i])
        right_i += 1
    return result

print(merge_sort(lst))
