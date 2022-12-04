# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import os
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()
import math
my_pi = 3
n = float(input("Введите необхидимую точность в виде десятичной дроби: "))
y=2
x = 1
while abs(my_pi - math.pi) > n:
    
    if x == 1:
        my_pi = my_pi + 4 / (y * (y + 1) * (y + 2))
        x = 2
        y += 2
    elif x == 2:
        my_pi = my_pi - 4 / (y * (y + 1) * (y + 2))
        x = 1
        y += 2
print(y)
print(my_pi)
print(math.pi)