# Дано число R и список A размера N. Найти элемент списка, который наиболее близок 
# к числу R (то есть такой элемент AK, для которого величина |AK - R| является 
# минимальной)

target_R = 25
list_A = [10, 30, 5, 40, 26, 24, 1, 50]

print("Список А:", list_A)
print("Значение R:", target_R)

if not list_A: #проверяем, что список не пуст
    closest_value = None
    print("Список пуст, ближайший элемент не найден.")
else:
    closest_value = list_A[0] - target_R
    min_difference = abs(list_A[0] - target_R) #abs() - функция, которая возвращает абсолютное значение (например, abs(-5) = 5)

    for element in list_A[1:]:
        current_difference = abs(element - target_R) #для каждого элемента вычисляем его разницу с R
        if current_difference < min_difference: #если текущая разница меньше, то мы нашли более близкий элемент
            min_difference = current_difference
            closest_value = element

    print("Ближайший элемент:", closest_value)
