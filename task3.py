# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
# https://drive.google.com/file/d/1n-kd763Dbw6N4ConxnHkuK2civQEhf-p/view?usp=sharing


letter_1 = ord(input('Введите букву(a-z): ').lower())
letter_2 = ord(input('Введите букву(a-z): ').lower())

print(abs(122 - (letter_1 + 26)))
print(abs(122 - (letter_2 + 26)))
print(letter_2 - letter_1 - 1)
