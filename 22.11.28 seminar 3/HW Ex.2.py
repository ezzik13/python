# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

import random

n = int(input("Введите желаемую длину списка: "))
lst1 = []

for i in range(n):
    lst1.append(random.randint(1, 10))
print(lst1)

# def pro_list(lst_):
#     result = []
#     for i in range(n/2):
#         result.append(lst_[i]*lst_[(-i) - 1])
#     print(result)
# pro_list(lst1)
lst2 = []
for i in range(len(lst1)):
    if i < len(lst1) / 2:
        lst2.append(lst1[i] * lst1[- i - 1])
print(lst2)
