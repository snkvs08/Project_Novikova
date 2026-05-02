#В матрице найти сумму и произведение элементов строки N (N задать с клавиатуры).

import random
from functools import reduce

n = int(input("Введите размер матрицы (n x n): "))
N = int(input("Введите номер строки: "))

matrix = [[random.randint(1, 100) for j in range(n)] for i in range(n)]

s = sum(matrix[N-1][j] for j in range(n))
k = (matrix[N-1][j] for j in range(n))
p = reduce(lambda x, y: x * y, k)

print("Матрица:", matrix)
print("Сумма:", s)
print("Произведение:", p)