""" 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах.
 Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
 lesson3 - 4. Определить, какое число в массиве встречается чаще всего. """


import sys
from random import randint


my_list = [randint(1, 10) for i in range(20)]


def show(obj):
    print(f'{type(obj) = }, {sys.getsizeof(obj) = } {obj =}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in object.items():
                show(key)
                show(value)
        else:
            for item in obj:
                show(item)


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

show(my_list)
show(max_val_dict)

"""             
type(obj) = <class 'list'>, sys.getsizeof(obj) = 248 obj =[2, 10, 3, 3, 7, 9, 7, 10, 3, 9, 6, 2, 4, 5, 4, 10, 1, 1, 2, 9]
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =2
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =10
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =3
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =3
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =7
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =9
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =7
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =10
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =3
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =9
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =6
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =2
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =4
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =5
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =4
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =10
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =1
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =1
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =2
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =9
type(obj) = <class 'function'>, sys.getsizeof(obj) = 136 obj =<function max_val_dict at 0x000002122C54A8B0>
"""