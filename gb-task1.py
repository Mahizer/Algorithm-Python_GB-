""" 1. В диапазоне натуральных чисел от 2 до 99 определить,
 сколько из них кратны каждому из чисел в диапазоне от 2 до 9. """


my_dict = {key: [] for key in range(2, 10)}

for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            my_dict[j].append(i)


for key, values in zip(my_dict.keys(), my_dict.values()):
    print(f'{key} = {values}')


