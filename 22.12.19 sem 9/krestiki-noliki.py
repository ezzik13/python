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
import emoji

# player_1 = input("Представьтесь, игрок №1: ")
# player_2 = input("Представьтесь, игрок №2: ")
player_1 = 1
player_2 = 2

figura = random.randint(0, 2)
if figura == 0:
    print(f'{player_1} играет ноликами, {player_2} играет крестиками ')
    s1 = ':hollow_red_circle:'
    s2 = ':cross_mark:'
    v1 = 'o'
    v2 = 'x'
else:
    print(f'{player_1} играет крестиками, {player_2} играет ноликами')
    s1 = ':cross_mark:'
    s2 = ':hollow_red_circle:'
    v1 = 'x'
    v2 = 'o'

lst1 = "1 | 2 | 3\n----------\n4 | 5 | 6\n----------\n7 | 8 | 9"
print(lst1)

hod = random.randint(0, 2)

vid = ":keycap_1:  |:keycap_2:  |:keycap_3: \n----------\n:keycap_4:  |:keycap_5:  |:keycap_6: \n----------\n:keycap_7:  |:keycap_8:  |:keycap_9: "    
print(emoji.emojize(vid))

for i in range(9):
    if hod == 0:
        print(f"ход игрока {player_1}")
        x = input('В какую ячейку сходим? ')
        for k, j in enumerate(lst1):
            if x == j:
                lst1 = lst1.replace(lst1[k], v1)
                print(lst1)
                hod = 1
                break

        if x == '1':
            vid = vid.replace(':keycap_1: ', s1)
        elif x == '2':
            vid = vid.replace(':keycap_2: ', s1)
        elif x == '3':
            vid = vid.replace(':keycap_3: ', s1)
        elif x == '4':
            vid = vid.replace(':keycap_4: ', s1)
        elif x == '5':
            vid = vid.replace(':keycap_5: ', s1)
        elif x == '6':
            vid = vid.replace(':keycap_6: ', s1)
        elif x == '7':
            vid = vid.replace(':keycap_7: ', s1)
        elif x == '8':
            vid = vid.replace(':keycap_8: ', s1)
        elif x == '9':
            vid = vid.replace(':keycap_9: ', s1)
        print(emoji.emojize(vid))
            
            
    else:
        print(f"ход игрока {player_2}")
        o = input('В какую ячейку сходим? ')
        for k, j in enumerate(lst1):
            if j == o:
                lst1 = lst1.replace(lst1[k], v2)
                print(lst1)
                hod = 0
                break

        if o == '1':
            vid = vid.replace(':keycap_1: ', s2)
        elif o == '2':
            vid = vid.replace(':keycap_2: ', s2)
        elif o == '3':
            vid = vid.replace(':keycap_3: ', s2)
        elif o == '4':
            vid = vid.replace(':keycap_4: ', s2)
        elif o == '5':
            vid = vid.replace(':keycap_5: ', s2)
        elif o == '6':
            vid = vid.replace(':keycap_6: ', s2)
        elif o == '7':
            vid = vid.replace(':keycap_7: ', s2)
        elif o == '8':
            vid = vid.replace(':keycap_8: ', s2)
        elif o == '9':
            vid = vid.replace(':keycap_9: ', s2)
        print(emoji.emojize(vid))
            
            
    
    if lst1[0] == lst1[4] == lst1[8] == v1:        
        print(emoji.emojize(f"{s1}{s1}{s1} :money_bag: Выигрывает {player_1} :money_bag:{s1}{s1}{s1}"))
        break
    elif lst1[42] == lst1[46] == lst1[50] == v1:
        print(emoji.emojize(f"{s1}{s1}{s1} :money_bag: Выигрывает {player_1} :money_bag:{s1}{s1}{s1}"))
        break
    elif lst1[4] == lst1[25] == lst1[46] == v1:
        print(emoji.emojize(f"{s1}{s1}{s1} :money_bag: Выигрывает {player_1} :money_bag:{s1}{s1}{s1}"))
        break
    elif lst1[0] == lst1[25] == lst1[50] == v1:
        print(emoji.emojize(f"{s1}{s1}{s1} :money_bag: Выигрывает {player_1} :money_bag:{s1}{s1}{s1}"))
        break
    elif lst1[21] == lst1[25] == lst1[29] == v1:        
        print(emoji.emojize(f"{s1}{s1}{s1} :money_bag: Выигрывает {player_1} :money_bag:{s1}{s1}{s1}"))
        break
    elif lst1[0] == lst1[21] == lst1[42] == v1:
        print(emoji.emojize(f"{s1}{s1}{s1} :money_bag: Выигрывает {player_1} :money_bag:{s1}{s1}{s1}"))
        break
    elif lst1[8] == lst1[29] == lst1[50] == v1:
        print(emoji.emojize(f"{s1}{s1}{s1} :money_bag: Выигрывает {player_1} :money_bag:{s1}{s1}{s1}"))
        break
    elif lst1[8] == lst1[25] == lst1[42] == v1:
        print(emoji.emojize(f"{s1}{s1}{s1} :money_bag: Выигрывает {player_1} :money_bag:{s1}{s1}{s1}"))
        break
    elif lst1[21] == lst1[25] == lst1[29] == v2:
        print(emoji.emojize(f"{s2}{s2}{s2} :money_bag: Выигрывает {player_2} :money_bag:{s2}{s2}{s2}"))
        break
    elif lst1[0] == lst1[21] == lst1[42] == v2:
        print(emoji.emojize(f"{s2}{s2}{s2} :money_bag: Выигрывает {player_2} :money_bag:{s2}{s2}{s2}"))
        break
    elif lst1[8] == lst1[29] == lst1[50] == v2:
        print(emoji.emojize(f"{s2}{s2}{s2} :money_bag: Выигрывает {player_2} :money_bag:{s2}{s2}{s2}"))
        break
    elif lst1[8] == lst1[25] == lst1[42] == v2:
        print(emoji.emojize(f"{s2}{s2}{s2} :money_bag: Выигрывает {player_2} :money_bag:{s2}{s2}{s2}"))
        break
    elif lst1[0] == lst1[4] == lst1[8] == v2:
        print(emoji.emojize(f"{s2}{s2}{s2} :money_bag: Выигрывает {player_2} :money_bag:{s2}{s2}{s2}"))
        break
    elif lst1[42] == lst1[46] == lst1[50] == v2:
        print(emoji.emojize(f"{s2}{s2}{s2} :money_bag: Выигрывает {player_2} :money_bag:{s2}{s2}{s2}"))
        break
    elif lst1[4] == lst1[25] == lst1[46] == v2:
        print(emoji.emojize(f"{s2}{s2}{s2} :money_bag: Выигрывает {player_2} :money_bag:{s2}{s2}{s2}"))
        break
    elif lst1[0] == lst1[25] == lst1[50] == v2:
        print(emoji.emojize(f"{s2}{s2}{s2} :money_bag: Выигрывает {player_2} :money_bag:{s2}{s2}{s2}"))
        break
    if i == 8:
        print(emoji.emojize(":crossed_swords::crossed_swords::crossed_swords:   НИЧЬЯ :crossed_swords::crossed_swords::crossed_swords:"))


