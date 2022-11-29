# Задайте список. Напишите программу, которая определит, присутствует ли в 
# заданном списке строк некое число.    ['22', '33', '123', 'fwefe', 'ytyy', '55'] 
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()


lst = ['22', '33', '123', 'fwefe', 'ytyy', '55']
number = int(input('Введите искомое число: '))               #int(input(f"{''}"))
for item in lst:
    if item.isdigit():
         if int(item) == number:
            print('yes')
            break
