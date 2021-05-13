""" 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах.
 Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
 7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться."""


import sys
from random import randint


my_list = [randint(-10, 25) for i in range(12)]


def show(obj):
    print(f'{type(obj) = }, {sys.getsizeof(obj) = } {obj = }')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in object.items():
                show(key)
                show(value)
        else:
            for item in obj:
                show(item)


def two_min_num(any_list):
    min_1, min_2 = any_list[0], any_list[0]
    for el in any_list:
        if el < min_1:
            min_1 = el
    for el2 in any_list:
        if min_1 < el2 < min_2:
            min_2 = el2
    return min_1, min_2

show(my_list)
show(two_min_num)

""" type(obj) = <class 'list'>, sys.getsizeof(obj) = 184 obj =[-5, 20, -5, 21, 1, 19, 8, 15, 20, -2, 11, -4]
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =-5
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =20
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =-5
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =21
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =1
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =19
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =8
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =15
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =20
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =-2
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =11
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =-4
type(obj) = <class 'function'>, sys.getsizeof(obj) = 136 obj =<function two_min_num at 0x000001CDED2214C0>"""