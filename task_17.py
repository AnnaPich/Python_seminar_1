# Задача 17:
# Дан список чисел. Определите, сколько в нем встречается различных чисел. 1 2 3 1 2 4 -> 4 (1 2 3 4)

list_1 = []
for i in range(5):
    list_1.append(int(input("Eter number: "))) # append - добавление элемента последним в список
print (f"{list_1} -> {len(set(list_1))} ({set(list_1)})")
