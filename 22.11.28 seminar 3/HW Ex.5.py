# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()
k = int(input('Введите число: ')) + 1
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib2(n):
    if n in [1, 2]:
        return 1
    else:
        return fib2(n + 2) - fib2(n + 1)

lst1 = []
for i in range(1, k):
    lst1.append(fib(i))
for i in range(0, -k, -1):
    lst1.insert(0, fib2(i))

print(lst1) 