# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все
# конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()
import random

player_1 = input("Представьтесь, игрок №1: ")
player_2 = 'bot_random'
hod = random.randint(0, 2)
if hod == 0:
    print(f'{player_1} ходит первый')
else:
    print(f'{player_2} ходит первый')

x = 2021
max_hod = 28
print(f'На Вашем столе {x} конфета, Вы можете за 1 ход забрать не более {max_hod}.')

while x > 0:
    if hod == 0:
        i = input(f'Ваш ход {player_1}, введите сколько конфет Вы забираета(от 1 до {max_hod}): ')
        if int(i) < 1 or int(i) > 28:
             i = 28
        else:
            i = int(i)
        x = x - i
        hod = 1
        cls()
        if x > 0:
            print(f'На столе осталось {x} конфет')
        else:
            print(f'Все конфеты достаются {player_1}')
    else:
        if x <= max_hod:
            j = x
        elif x % (max_hod+1) == 0:
            j = 1
        elif x % (max_hod+1) != 0:
            j = x % (max_hod+1)
        x = x - j
        hod = 0
        if x > 0:
            print(f'На столе осталось {x} конфет')
        else:
            print(f'Все конфеты достаются {player_2}')


