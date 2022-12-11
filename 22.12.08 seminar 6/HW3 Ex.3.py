# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()
# Было:
# lst1 = [1.1, 1.2, 3.1, 5, 10.01]

# for i in lst1:
#     if isinstance(i, int) == True:
#         lst1.remove(i)
# for i in range(len(lst1)):
#         lst1[i] = round((lst1[i] - int(lst1[i])), 2)

# print(lst1)
# max = 0
# min = 1

# for i in lst1:
#     if i > max:
#         max = i
#     if i < min:
#         min = i
# print(max - min)
#  
# 
# Предложить улучшения кода для четырёх уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# Начиная с 3 семинара. 
# применил лямбды, filter, map:



lst1 = [1.1, 1.2, 3.1, 5, 10.01]

lst2 = list(filter(lambda x: not type(x) == int, lst1))
def func(x):
    x = round(x - int(x), 2)
    return x
lst3 = list(map(func, lst2))

print(lst1)
print(lst2)
print(lst3)
print(max(lst3) - min(lst3))