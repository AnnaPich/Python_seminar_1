# Задача 9:
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу, используя цикл while
# Input: 5
# Output: 120

n = int(input("Enter number: "))

if n > 0:
    i = 1
    mult = 1
    while i <= n:
        mult *= i  # = mult = mult * i
        i += 1
    print(mult)
elif n == 0:
    print(1)
else:
    print("Error! Invalid number!")
