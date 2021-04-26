# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.


number = int(input())
num_sum = 0

for i in range(1, number + 1):
    num_sum += i

if num_sum == number * (number + 1) / 2:
    print('YES')
else:
    print('NO')