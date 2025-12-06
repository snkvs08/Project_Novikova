# Дано число R и список A размера N. Найти элемент списка, который наиболее близок 
# к числу R (то есть такой элемент AK, для которого величина |AK - R| является 
# минимальной)

import random

N = int(input("Введите размер списка: "))
R = int(input("Введите число R: "))
list_a = []
while len (list_a) <= N:
    list_a.append(random.randint(1,50))

print("Список А:", list_a)
print("Значение R:", R)

if not list_a: #проверяем, что список не пуст
    closest_value = None
    print("Список пуст, ближайший элемент не найден.")
else:
    closest_value = list_a[0] - R
    min_difference = abs(list_a[0] - R) #abs() - функция, которая возвращает абсолютное значение (например, abs(-5) = 5)

    for element in list_a[1:]:
        current_difference = abs(element - R) #для каждого элемента вычисляем его разницу с R
        if current_difference < min_difference: #если текущая разница меньше, то мы нашли более близкий элемент
            min_difference = current_difference
            closest_value = element

    print("Ближайший элемент:", closest_value)
