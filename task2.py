""" 2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

from timeit import timeit
import cProfile


def prime_numbers(num):
    my_list = [i for i in range(2, num+1)]
    new_list = []
    for i in my_list:
        if i == 2 or i == 3:
            new_list.append(i)
        elif i % 2 == 0 or i % 3 == 0:
            continue
        else:
            new_list.append(i)

    return new_list

print(prime_numbers(100))
print(timeit('prime_numbers(100)', number=100, globals=globals()))       # 0.00031890000000001084
print(timeit('prime_numbers(1000)', number=100, globals=globals()))      # 0.03870069999999999
print(timeit('prime_numbers(10000)', number=100, globals=globals()))     # 0.3653491
print(timeit('prime_numbers(100000)', number=100, globals=globals()))    # 3.7510035000000004




