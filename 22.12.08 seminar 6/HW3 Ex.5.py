# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# применил list comprehension:

k = int(input('Введите число: '))
def fib(n):
    if n in [1, 2]:
        return 1
    elif n > 2:
        return fib(n-1) + fib(n-2)
    elif n < 1:
        return fib(n + 2) - fib(n + 1)

lst1 = [fib(i) for i in range(-k, k+1)] # стало!!!
# for i in range(-k, k):  Было!!!
#     lst1.append(fib(i))

print(lst1) 
