# 3 Создайте программу для игры в "Крестики-нолики".

# Вариант интерфейса:

#  1  |  2 | 3
# --------------
#  4  |  5 | 6
# --------------
#  7  |  8 | 9
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()
import random

player_1 = input("Представьтесь, игрок №1: ")
player_2 = input("Представьтесь, игрок №2: ")

figura = random.randint(0, 2)
if figura == 0:
    print(f'{player_1} играет ноликами, {player_2} играет крестиками ')
    s1 = 'O'
    s2 = 'X'
else:
    print(f'{player_1} играет крестиками, {player_2} играет ноликами')
    s1 = 'X'
    s2 = 'O'

lst1 = "1 | 2 | 3\n----------\n4 | 5 | 6\n----------\n7 | 8 | 9"
print(lst1)

hod = random.randint(0, 2)

    


for i in range(9):
    if hod == 0:
        print(f"ход игрока {player_1}")
        x = input('В какую ячейку сходим? ')
        for k, j in enumerate(lst1):
            if j == x:
                lst1 = lst1.replace(lst1[k], s1)
                print(lst1)
                hod = 1
                break
            
    else:
        print(f"ход игрока {player_2}")
        o = input('В какую ячейку сходим? ')
        for k, j in enumerate(lst1):
            if j == o:
                lst1 = lst1.replace(lst1[k], s2)
                print(lst1)
                hod = 0
                break
            
    
    if lst1[0] == lst1[4] == lst1[8] == s1 or lst1[21] == lst1[25] == lst1[29] == s1:
        print(f"{player_1} выйграл")
        break
    elif lst1[42] == lst1[46] == lst1[50] == s1 or lst1[0] == lst1[21] == lst1[42] == s1:
        print(f"{player_1} выйграл")
        break
    elif lst1[4] == lst1[25] == lst1[46] == s1 or lst1[8] == lst1[29] == lst1[50] == s1:
        print(f"{player_1} выйграл")
        break
    elif lst1[0] == lst1[25] == lst1[50] == s1 or lst1[8] == lst1[25] == lst1[42] == s1:
        print(f"{player_1} выйграл")
        break
    elif lst1[0] == lst1[4] == lst1[8] == s2 or lst1[21] == lst1[25] == lst1[29] == s2:
        print(f"{player_2} выйграл")
        break
    elif lst1[42] == lst1[46] == lst1[50] == s2 or lst1[0] == lst1[21] == lst1[42] == s2:
        print(f"{player_2} выйграл")
        break
    elif lst1[4] == lst1[25] == lst1[46] == s2 or lst1[8] == lst1[29] == lst1[50] == s2:
        print(f"{player_2} выйграл")
        break
    elif lst1[0] == lst1[25] == lst1[50] == s2 or lst1[8] == lst1[25] == lst1[42] == s2:
        print(f"{player_2} выйграл")
        break
    if i == 8:
        print("ничья")
    



        



