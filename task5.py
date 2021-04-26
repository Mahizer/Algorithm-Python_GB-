# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

# https://drive.google.com/file/d/1n-kd763Dbw6N4ConxnHkuK2civQEhf-p/view?usp=sharing

for i in range(32, 128):
    print(f'{i} - {chr(i)}', end=',    ')
    if i % 10 == 1 or i % 100 == 1:
        print('\n')