# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

n = int(input("Введите число "))

lst_mn = []
while n > 1:
    for i in range(2, n+1):    
        if n % i == 0:
            lst_mn.append(i)
            n = n // i
            break
        
    
print(lst_mn)
