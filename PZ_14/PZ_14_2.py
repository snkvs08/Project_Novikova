#Из двух чисел вывести большее.
from tkinter import *

def num():
    a = int(num1.get())
    b = int(num2.get())
    result.config(text="Большее: " + str(max(a, b)))

root = Tk()
root.title("Сравнение чисел")

Label(root, text="Первое число").pack()
num1 = Entry(root)
num1.pack()

Label(root, text="Второе число").pack()
num2 = Entry(root)
num2.pack()

Button(root, text="Найти большее", command=num).pack()

result = Label(root, text="")
result.pack()

root.mainloop()