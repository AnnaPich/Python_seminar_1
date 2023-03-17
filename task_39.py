# Задача 39:
# Даны два массива чисел.
# Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве),
# которых нет во втором массиве. Пользователь вводит первый массив через пробел
# и второй через пробел на разных строках.
# [1, 2, 3, 4, 5]
# [1, 2, 3] -> [4, 5]

def find_unique_element(list_first, list_second):
    resalt = ""
    for item in list_first:
        if item not in list_second:
            resalt += f'{item} '
    print(resalt)


list_first = list(map(int, input("Enter a first list of integers separated by a space: ").split()))
list_second = list(map(int, input("Enter a second list of integers separated by a space: ").split()))

find_unique_element(list_first, list_second)
# print(list_first.difference(list_second))
