# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# https://drive.google.com/file/d/1n-kd763Dbw6N4ConxnHkuK2civQEhf-p/view?usp=sharing


num = int(input('Введите целое трехзначное число: '))

num_1 = num // 100
num_2 = num //10 % 10
num_3 = num % 10
print(num_1 + num_2 + num_3, num_1 * num_2 * num_3, sep='\n')