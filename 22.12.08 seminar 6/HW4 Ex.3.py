# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()
# применил лямбды, filter:

lst1 = [1, 1, 2, 3, 4, 2, 3, 8, 5, 1, 4]
lst2 = list(filter(lambda x: lst1.count(x) == 1, lst1))   # СТАЛО!!!
# lst2 = []                       БЫЛО!!!!
# for i in lst1:
#     count = lst1.count(i)
#     if count == 1:
#         lst2.append(i)
    
print(lst2)

