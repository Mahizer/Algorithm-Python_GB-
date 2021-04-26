# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# https://drive.google.com/file/d/1n-kd763Dbw6N4ConxnHkuK2civQEhf-p/view?usp=sharing

user_num = input('Введите число: ')
sum_even = 0
sum_odd = 0

for i in user_num:
    if int(i) % 2 == 0:
        sum_even += 1
    else:
        sum_odd += 1

print(f'Сумма четных цифр: {sum_even}\nСумма нечетных цифр: {sum_odd}')
