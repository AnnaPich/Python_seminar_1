# Задача 23:
# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)
# 1 2 3 4 3 2 1 -> 3 (2 , 3 , 4)
from random import randint

n = int(input("Enter number : "))

list_1 = [randint(0, 9) for i in range(n)]
list_2 = []
for i in range(1, n):
    if list_1[i] > list_1 [i-1]:
        list_2.append(list_1[i])
print(f'{list_1} -> {len(list_2)} ({list_2})')