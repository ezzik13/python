# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

lst1 = [1.1, 1.2, 3.1, 5, 10.01]

for i in lst1:
    if isinstance(i, int) == True:
        lst1.remove(i)
for i in range(len(lst1)):
        lst1[i] = round((lst1[i] - int(lst1[i])), 2)

print(lst1)
max = 0
min = 1

for i in lst1:
    if i > max:
        max = i
    if i < min:
        min = i
print(max - min)
