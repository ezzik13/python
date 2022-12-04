# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

import random

k = int(input("Введите степень многочлена К: "))
lst_r = []
lst_p = []
for i in range(k+1):
    lst_r.append(random.randint(1, 100))
    lst_p.append(random.randint(0, k-1))
# print(lst_p)
lst_p = set(lst_p)
lst_p = [*lst_p]
# print(lst_r)
# print(lst_p)
str_1 = (f"{lst_r[len(lst_r)-1]} * x ** {k}")

for i in range(len(lst_p)-1, -1, (-1)):
    if lst_p[i] > 1:
        str_1 = str_1 + (f" + {lst_r[i]} * x ** {lst_p[i]}")
    elif lst_p[i] == 1:
        str_1 = str_1 + (f" + {lst_r[i]} * x")
    elif lst_p[i] == 0:
        str_1 = str_1 + (f" + {lst_r[i]}")

str_1 = str_1 + (" = 0")
    
print(str_1)

with open("file2.txt", "w") as file1:
    file1.write(str_1)