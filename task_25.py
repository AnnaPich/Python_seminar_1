# Задача 23:
# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался. Количество повторов добавляется
# к символам с помощью постфикса формата _n.
# Пример: Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2


text = input("Enter a text: ")

#text_1 =set(text)
# Вариант 1:
# for i in range(len(text_1)):
#     simbol = text[i]
#     count = 0
#     for k in range(len(text)):
#         if text[k] == simbol:
#             count += 1
#     print(f"{simbol}_{count}")

# Вариант 2:
# for i in text_1:
#     count = 0
#     for k in text:
#         if k == i:
#             count += 1
#     print(f"{i}_{count}")

# Вариант 3: работает не всегда
#Решение через срезы:

new_string = ''
sdvig = 0
for i in text.split():
    if text[0:sdvig].count(i) != 0:
        new_string += f'{i}_{text[0:sdvig].count(i)} '
    else:
        new_string += f'{i} '
    sdvig += 2
print(new_string)

