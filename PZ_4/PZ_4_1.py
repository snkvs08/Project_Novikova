# Дано целое число N (>0). Найти произведение 1.1 • 1.2 • 1.3 •... (N сомножителей).

while True:
    n = input("Введите целое число N (N > 0): ")
    try:
        N = int(n)
        if N > 0:
            break
        else:
            print("Введённое число должно быть больше 0. Пожалуйста, введите положительное число.")
    except ValueError:
        print("Ошибка. Введённое число не целое. Пожалуйста, введите целое положительное число.")

multiplication = 1.0
current_multiplier = 1.1
counter = 0

while counter < N:
    multiplication *= current_multiplier
    current_multiplier += 0.1
    counter += 1

print("Произведение:", multiplication)