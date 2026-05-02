#В матрице найти сумму элементов второй половины матрицы.

import random

n = int(input("Введите чётный размер матрицы (n x n): "))

if n % 2 != 0:
    print("Ошибка: размер матрицы должен быть четным числом!")
else:
    matrix = [[random.randint(1, 100) for j in range(n)] for i in range(n)]

    s = sum(matrix[i][j] for i in range(n) for j in range(n//2, n))

    print("Матрица:", matrix)
    print("Сумма элементов второй половины матрицы:", s)