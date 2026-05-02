#В матрице найти сумму элементов второй половины матрицы.

import random

n = int(input("Введите количество строк: "))
c = int(input("Введите количество столбцов: "))

if c % 2 != 0:
    print("Ошибка: количество столбцов должно быть четным числом!")
else:
    matrix = [[random.randint(1, 100) for j in range(c)] for i in range(n)]

    s = sum(matrix[i][j] for i in range(n) for j in range(c//2, c))

    print("Матрица:", matrix)
    print("Сумма элементов второй половины матрицы:", s)