# Задача №15.
# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза

# Input: 5 -> 5 1 6 5 9
# Output: 1 9

number_watermelons = int(input("Enter number of watermelons: "))
i = 0
max = 0
min = 100
while i < number_watermelons:
    weight_watermelons = int(input("Enter weight of watermelon: "))
    if weight_watermelons > max:
        max = weight_watermelons
    if weight_watermelons < min:
        min = weight_watermelons
    i+=1
print(f"Max weight:{max}, min weight: {min}")
