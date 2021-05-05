from timeit import timeit
import cProfile


def eratosthenes(num):
    sieve = [i for i in range(num + 1)]
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    sieve = set(sieve)
    sieve.remove(0)
    return sieve

print(eratosthenes(100))
print(timeit('eratosthenes(100)', number=100, globals=globals()))      # 0.004251900000000003
print(timeit('eratosthenes(1000)', number=100, globals=globals()))     # 0.049104400000000006
print(timeit('eratosthenes(10000)', number=100, globals=globals()))    # 0.5264986
print(timeit('eratosthenes(100000)', number=100, globals=globals()))   # 5.3950767

cProfile.run('eratosthenes(100)')

""" Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task2-eratosfen.py:5(eratosthenes)
        1    0.000    0.000    0.000    0.000 task2-eratosfen.py:6(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       25    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'remove' of 'set' objects}

"""

