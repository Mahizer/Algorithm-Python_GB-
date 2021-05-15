""" 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее)."""

from random import randint


lst = [randint(-100, 99) for _ in range(12)]
print(lst)


def bubble_sort(list_):
    for j in range(1, len(list_)):
        for i in range(len(list_) - j):
            if list_[i] > list_[i + 1]:
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
    list_.reverse()
    return list_

print(bubble_sort(lst))
