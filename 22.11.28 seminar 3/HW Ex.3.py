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
max1 = 0
min1 = 1

for i in lst1:
    if i > max1:
        max1 = i
    if i < min1:
        min1 = i
print(max1 - min1)
