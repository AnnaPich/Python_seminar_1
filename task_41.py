# Задача 41:
# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Элементы массива вводятся на одной строке через пробел. Массив состоит из целых чисел. Список нецикличный
# [1, 2, 1, 3, 4, 3] -> 2 (2, 4)

from random import randint

n = int(input("Enter number : "))

list_1 = [randint(0, 9) for i in range(n)]
list_2 = []

if n >= 3:
    for i in range(1, n - 1):
        if list_1[i] > list_1[i - 1] and list_1[i] > list_1[i + 1]:
            list_2.append(list_1[i])
    print(f'{list_1} - > {len(list_2)} {list_2}')
else:
    print("Error")

