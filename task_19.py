# Задача 19:
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,
# K – положительное число. 1 2 3 4 5 K = 3 -> 3 4 5 1 2

from random import randint

n = int(input("Enter number N: "))
k = 3
list_1 = [randint(0, 9) for i in range(n)]
print(list_1)

for i in range(k):
    # temp = list_1.pop() # псследний элемент списка
    # list_1.insert(0,temp) # добавление элемента temp на позицию 0
    list_1.insert(0, list_1.pop())
print(list_1)
