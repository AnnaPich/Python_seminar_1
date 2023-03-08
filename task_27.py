# Задача 27:
# Пользователь вводит текст(строка).
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.


text = input("Enter a text: ")

# Вариант 1
# simbol = " "
# word = list()
# words_array = list()
#
# for i in range(len(text)):
#     if text[i] != simbol:
#         word.append(text[i])
#     else:
#         words_array.append(word)
#         word = list()
#     if i == len(text) - 1:
#         words_array.append(word)
#
# print(words_array)
# print(len(words_array))

# Вариант 2

words_array = set(text.lower().split())

print(f'{words_array} -> {len(words_array)}')


