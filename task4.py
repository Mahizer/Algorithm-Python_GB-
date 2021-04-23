# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# https://drive.google.com/file/d/1n-kd763Dbw6N4ConxnHkuK2civQEhf-p/view?usp=sharing

user_letter = ord(input('Введите букву(a-z): ').lower())

print(abs(122 - (user_letter + 26)))
 