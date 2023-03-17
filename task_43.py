# Задача 43:
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу, образуют одну пару, которую необходимо посчитать.
# Вводится список чисел через пробел в одну строку. (сочетания без повторений)
# [2, 2, 2, 2] -> 6

def find_pairs(list_1, n):
    list_2 = list()
    if n >= 2:
        for i in range(n):
            count = 0
            for k in range(i, n):
                if list_1[k] == list_1[i]:
                    count += 1
            list_2.append(count)
        return (max(list_2))
    else:
        print('error!')


def numb_pairs(x):  # вариант решения через рекурсию
    if x != 0:
        return (x + numb_pairs(x - 1))
    else:
        return (-x)


from random import randint

n = int(input("Enter number: "))

list_1 = [randint(1, 2) for i in range(n)]

max_numb_elements = find_pairs(list_1, n)

print(f'{list_1} -> {numb_pairs(max_numb_elements - 1)}')  # вариант 1
print(f'{list_1} -> {int((max_numb_elements-1) / 2 * max_numb_elements)}')  # вариант 2
