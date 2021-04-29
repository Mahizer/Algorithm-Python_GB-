""" 2. Во втором массиве сохранить индексы четных элементов первого массива.
 Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
 то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
  т.к. именно в этих позициях первого массива стоят четные числа."""


from random import randint

my_list = [randint(1, 100) for _ in range(10)]
index_list = []

for inx, val in zip([i for i in range(0, len(my_list)+1)], my_list):
    if val % 2 == 0:
        index_list.append(inx)


print(my_list, index_list, sep='\n')
