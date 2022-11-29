# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

n = int(input('Введите число: '))
n_bin = []
while n > 0:
    n_bin.append(n % 2)
    n = n // 2
n_bin.reverse()
print(*n_bin, sep="")