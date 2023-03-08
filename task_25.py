# Задача 23:
# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался. Количество повторов добавляется
# к символам с помощью постфикса формата _n.

text = input("Enter a text: ")

text_1 =set(text)

for i in range(len(text_1)):
    simbol = text[i]
    count = 0
    for k in range(len(text)):
        if text[k] == simbol:
            count += 1
    print(f"{simbol}_{count}")

