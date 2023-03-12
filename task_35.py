# Задача 35.
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n (само число)

def prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            print("The number is not prime number")
            return
    print("The number is prime number")

number = int(input("Enter number: "))
if number > 1:
    prime_number(number)
