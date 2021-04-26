# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125
# ...Количество элементов (n) вводится с клавиатуры.

# https://drive.google.com/file/d/1n-kd763Dbw6N4ConxnHkuK2civQEhf-p/view?usp=sharing

number = int(input('Введите число: '))
number_sum = 0
divider = 1

for i in range(number):
    if i % 2 == 0:
        number_sum += divider
    else:
        number_sum -= divider
    divider /= 2

print('%.4f' % number_sum)

