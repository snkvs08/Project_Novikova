import random
A = [random.randint(-100, 100) for i in range(10)]
B = [i for i in A if (i < 0) and (i % 5 == 0)]

print("Список А:", A)
print("Список B:", B)
print("Количество чисел списка B:", len(B))
