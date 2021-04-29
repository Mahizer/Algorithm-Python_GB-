""" 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы. """

from random import randint


my_list = [[randint(1, 100) for i in range(4)] for _ in range(4)]
new_list = []
max_num = 0


for i in range(4):
    min_num = 100
    for j in my_list[i]:
        if j < min_num:
            min_num = j
    new_list.append(min_num)

for el in new_list:
    if el > max_num:
        max_num = el


print('Матрица: ', *my_list, sep='\n', end='\n\n')
print(f'Минимальные элементы столбцов: {new_list}')
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_num}')

