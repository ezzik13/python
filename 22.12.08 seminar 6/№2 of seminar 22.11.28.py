# Задайте список. Напишите программу, которая определит, присутствует ли в 
# заданном списке строк некое число.    ['22', '33', '123', 'fwefe', 'ytyy', '55'] 
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# Начиная с 3 семинара. 
# применил лямбды, filter:

number = int(input('Введите искомое число: '))

for x in filter(lambda x: x.isdigit() == True, ['22', '33', '123', 'fwefe', 'ytyy', '55']):   #  СТАЛО!!!
    if int(x) == number:
        print('yes')

        
# lst1 = ['22', '33', '123', 'fwefe', 'ytyy', '55']       БЫЛО!!!
# for item in lst:                  
#     if item.isdigit():
#          if int(item) == number:
#             print('yes')
#             break
