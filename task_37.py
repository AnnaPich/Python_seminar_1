# Задача 37.
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.

def reverse(numb):
    if numb == 1:
        print(numb)
    else:
        print(numb, end=', ')
        reverse(numb - 1)

reverse(int(input("Enter number: ")))
