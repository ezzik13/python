# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

lst1 = [1, 1, 2, 3, 4, 2, 3, 8, 5, 1, 4]
lst2 = []
for i in lst1:
    count = lst1.count(i)
    # count = 0
    # for j in lst1:
    #     if j == i:
    #         count += 1
    if count == 1:
        lst2.append(i)
    
print(lst2)

