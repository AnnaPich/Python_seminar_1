# Задача 33.
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
#
# [1, 1, 1, 3, 2, 5, 5] -> [1, 1, 1, 3, 2, 1, 1]
#
# [2, 3, 4, 10 , 10, 2] -> [2, 3, 4, 2 , 2, 2]


from random import randint
numbers = [randint (1,10) for i in range(10)]
print(numbers)

low = min(numbers)
high = max(numbers)

for i in range(len(numbers)):
    if numbers[i] == high:
        numbers[i] = low
print(numbers)

