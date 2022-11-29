# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random
import os
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

n = int(input("Введите желаемую длину списка: "))
lst1 = []
sum = 0

for i in range(n):
    lst1.append(random.randint(1, 100))
print(lst1)

for i in range(1, len(lst1), 2):
    sum = sum + lst1[i]
print(sum)
