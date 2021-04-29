""" 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве."""

from random import randint


my_list = [randint(-60, 60) for i in range(20)]
max_negative_num = -9999

for i in my_list:
    if max_negative_num < i < 0:
        max_negative_num = i

print(my_list)
print(f'index = {my_list.index(max_negative_num)}, {max_negative_num = }')
