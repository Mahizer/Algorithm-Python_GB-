# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или
# меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.

# https://drive.google.com/file/d/1n-kd763Dbw6N4ConxnHkuK2civQEhf-p/view?usp=sharing

from random import randint


attempt = 0
random_number = randint(0, 100)

for i in range(10):
    user_number = int(input('Угадайте загаданное число(от 0 до 100): '))
    attempt += 1
    if random_number == user_number:
        print(f'Вы угадали число за {attempt} попыток')
        break
    elif random_number > user_number:
        print(f'{attempt} попытка.\n Ваше число меньше.')
    elif random_number < user_number:
        print(f'{attempt} попытка.\n Ваше число больше.')
    if attempt == 10:
        print(f'Вы не угадали. Загаданное число {random_number}')
