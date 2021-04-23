# 7. По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он
# разносторонним, равнобедренным или равносторонним.

# https://drive.google.com/file/d/1n-kd763Dbw6N4ConxnHkuK2civQEhf-p/view?usp=sharing

print('Введите длину трех отрезков: ')
side_a, side_b, side_c = int(input()), int(input()), int(input())

if (side_a + side_b > side_c) and (side_a - side_b < side_c):
    if side_a != side_b and side_a != side_c and side_b != side_c:
        print('Разносторонний')
    elif side_c == side_b == side_a:
        print('Равносторонний')
    else:
        print('Равнобедренний')
else:
    print('Не треугольник')