# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

# https://drive.google.com/file/d/1n-kd763Dbw6N4ConxnHkuK2civQEhf-p/view?usp=sharing

num_1, num_2, num_3 = int(input()), int(input()), int(input())

if num_1 <= num_2 <= num_3 or num_3 <= num_2 <= num_1:
    print(num_2)
elif num_2 <= num_1 <= num_3 or num_3 <= num_1 <= num_2:
    print(num_1)
else:
    print(num_3)
