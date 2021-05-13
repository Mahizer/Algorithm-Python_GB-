""" lesson3 - 1. В диапазоне натуральных чисел от 2 до 99 определить,
 сколько из них кратны каждому из чисел в диапазоне от 2 до 9. """

import sys


my_dict = {key: [] for key in range(2, 10)}


def show(obj):
    print(f'{type(obj) = }, {sys.getsizeof(obj) = } {obj =}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                show(key)
                show(value)
        else:
            for item in obj:
                show(item)


def my_def(any_dict):
    for i in range(2, 100):
        for j in range(2, 10):
            if i % j == 0:
                any_dict[j].append(i)

    for key, values in zip(any_dict.keys(), any_dict.values()):
        print(f'{key} = {values}')


show(my_dict)

""" type(obj) = <class 'dict'>, sys.getsizeof(obj) = 360 obj ={2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =2
type(obj) = <class 'list'>, sys.getsizeof(obj) = 56 obj =[]
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =3
type(obj) = <class 'list'>, sys.getsizeof(obj) = 56 obj =[]
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =4
type(obj) = <class 'list'>, sys.getsizeof(obj) = 56 obj =[]
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =5
type(obj) = <class 'list'>, sys.getsizeof(obj) = 56 obj =[]
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =6
type(obj) = <class 'list'>, sys.getsizeof(obj) = 56 obj =[]
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =7
type(obj) = <class 'list'>, sys.getsizeof(obj) = 56 obj =[]
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =8
type(obj) = <class 'list'>, sys.getsizeof(obj) = 56 obj =[]
type(obj) = <class 'int'>, sys.getsizeof(obj) = 28 obj =9
type(obj) = <class 'list'>, sys.getsizeof(obj) = 56 obj =[]
"""
