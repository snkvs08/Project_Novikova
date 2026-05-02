#В матрице найти сумму и произведение элементов строки N (N задать с клавиатуры).

import random
from functools import reduce

n = int(input("Введите количество строк: "))
c = int(input("Введите количество столбцов: "))

N = int(input("Введите номер строки: "))

matrix = [[random.randint(1, 3) for j in range(n)] for i in range(c)]

s = sum(matrix[N-1][j] for j in range(n))
k = (matrix[N-1][j] for j in range(n))
p = reduce(lambda x, y: x * y, k)

print("Матрица:", matrix)
print("Сумма:", s)
print("Произведение:", p)