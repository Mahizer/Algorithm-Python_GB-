# 4. Написать программу, которая генерирует в указанных пользователем границах

from random import randint, uniform

# https://drive.google.com/file/d/1n-kd763Dbw6N4ConxnHkuK2civQEhf-p/view?usp=sharing
start_str = ord(input('Введите начало границы(буква): ').lower())
stop_str = ord(input('Введите конец границы(буква): ').lower())
print(chr(randint(start_str, stop_str)))

# https://drive.google.com/file/d/1n-kd763Dbw6N4ConxnHkuK2civQEhf-p/view?usp=sharing
start_int = int(input('Введите начало границы(число): '))
stop_int = int(input('Введите конец границы(число): '))
print(randint(start_int, stop_int))

# https://drive.google.com/file/d/1n-kd763Dbw6N4ConxnHkuK2civQEhf-p/view?usp=sharing
start_float = float(input('Введите начало границы(дробное число): '))
stop_float = float(input('Введите конец границы(дробное число): '))
print(round((uniform(start_float, stop_float)), 2))

