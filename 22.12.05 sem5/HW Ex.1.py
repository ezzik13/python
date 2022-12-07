#  Напишите программу, удаляющую из файла все слова, содержащие "абв".
import os
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()
# str_1 = 'привет Абв пока абвг еще аббв'
# with open("files/f1 for l5.txt", "w") as file1:
#     file1.write(str_1)


with open("files/f1 for l5.txt", "r") as data:
    str0 = data.read().split()
with open("files/f1 for l5.txt", "r") as data:
    str1 = ' '.join(list(filter(lambda x: not 'абв' in x.lower(), data.read().split())))
print(str0)
print(str1)