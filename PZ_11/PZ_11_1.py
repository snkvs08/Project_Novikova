#В последовательности на n целых чисел найти и вывести:
#1. минимальный среди положительных
#2. элементы кратные пяти
#3. их среднее арифметическое

import random
from functools import reduce

n = int(input("Введите количество чисел: "))
a = [random.randint(-100, 100) for i in range(n)]

m = [i for i in a if i > 0]

k = [i for i in a if i % 5 == 0]
s = reduce (lambda x, y: x + y, k)

print("Последовательность:", a)
print("Минимальный среди положительных:", min(m))
print("Элементы, кратные пяти:", k)
print("Среднее арифметическое кратных пяти:", s / len(k))
