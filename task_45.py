# ЗАдача 45:
# Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 10^5.
# Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# 220 -> sum(1, 2, 4, 5, 10, 11, 20, 22, 44, 55,  110 ) = 284
# 284 -> sum(1, 2, 4, 71,  142) = 220

def sum_dividers_numb(k):
    sum_numb = 0
    for i in range(1, k):
        if k % i == 0:
            sum_numb = sum_numb + i
    return (sum_numb)

def list_dividers_numb(k):
    dividers = list()
    for i in range(1, k):
        if k % i == 0:
            dividers.append(i)
    print(f' -> {dividers} = {k}')

numb_k = int(input("Enter a number k: "))

if numb_k >= 10 ** 5:
    print("Error! Enter a number less than 10^5")

for i in range (1, numb_k):
    if i == sum_dividers_numb(sum_dividers_numb(i)) and i != sum_dividers_numb(i) and i < sum_dividers_numb(i):
        print(i, end='')
        list_dividers_numb(sum_dividers_numb(i))
        print(sum_dividers_numb(i), end='')
        list_dividers_numb(sum_dividers_numb(sum_dividers_numb(i)))
    elif i == 0:
        print("Thera not friendly numbers")