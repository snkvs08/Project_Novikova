#Из предложенного текстового файла (text18-11.txt) вывести на экран его содержимое,
#количество знаков препинания. Сформировать новый файл, в который поместить строку
#наименьшей длины.

try:
    file = open("c:/Users/ПК/Desktop/РКСИ 2 курс/Project_Novikova/PZ_10/text18-11.txt", "r", encoding="utf-16")
    k = file.readlines()
    file.close()
except FileNotFoundError:
    print("Файл не найден")
    exit()

print("Содержимое исходного файла: ")
for i in range(len(k)):
    print(k[i].rstrip())
m = 0
s = ",.()!?:;-''" 
for i in range(len(k)):
    for j in range (len(k[i])):
        if k[i][j] in s:
            m += 1
print("Количество знаков препинания:", m)

f1 = open("new.txt", "w", encoding="utf-16")
min_len = len(k[0]) if k else 0
min_str = ""

for i in k:
    if len(i) < min_len:
        min_len = len(i)
        min_str = i.rstrip()
if min_str:
    f1.write (str(min_str))
else:
    f1.write ("Строка наименьшей длины не найдена")

f1.close()
print("Строка наименьшей длины: ", min_str)
