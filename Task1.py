""" 1. Проанализировать скорость и сложность одного любого алгоритма,
 разработанных в рамках домашнего задания первых трех уроков.
 Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
 lesson2 - task3
"""

from timeit import timeit
import cProfile


def reverse_(num):
    new_number = ''

    for i in num:
        new_number = i + new_number

    return new_number


print(timeit('reverse_("76")', number=100, globals=globals()))         # 5.929999999999824e-05
print(timeit('reverse_("2345")', number=100, globals=globals()))       # 8.909999999999474e-05
print(timeit('reverse_("63456")', number=100, globals=globals()))      # 0.00010349999999999249
print(timeit('reverse_("125435")', number=100, globals=globals()))     # 0.00011919999999999986
print(timeit('reverse_("5343577")', number=100, globals=globals()))    # 0.0001350999999999991


cProfile.run('reverse_("76")')

""" 
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 Task1.py:11(reverse_)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


def d_reverse(num):
    return reverse_(num)


print(timeit('d_reverse("76")', number=100, globals=globals()))         # 7.509999999999462e-05
print(timeit('d_reverse("2345")', number=100, globals=globals()))       # 0.00010999999999999899
print(timeit('d_reverse("63456")', number=100, globals=globals()))      # 0.0001352999999999771
print(timeit('d_reverse("125435")', number=100, globals=globals()))     # 0.00014339999999998798
print(timeit('d_reverse("5343577")', number=100, globals=globals()))    # 0.0001633000000000051


cProfile.run('d_reverse("76")')

"""  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 Task1.py:11(reverse_)
        1    0.000    0.000    0.000    0.000 Task1.py:38(d_reverse)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects} """


