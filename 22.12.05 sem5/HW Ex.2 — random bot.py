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
        i = int(input(f'Ваш ход {player_1}, введите сколько конфет Вы забираета(от 1 до {max_hod}): '))
        if i < 1 or i > 28: i = 28
        x = x - i
        hod = 1
        cls()
        if x > 0:
            print(f'На столе осталось {x} конфет')
        else:
            print(f'Все конфеты достаются {player_1}')
    else:
        i = random.randint(1,max_hod + 1)
        x = x - i
        hod = 0
        cls()
        if x > 0:
            print(f'На столе осталось {x} конфет')
        else:
            print(f'Все конфеты достаются {player_2}')


# from random import randint
 
# CANDIES = 2022
# MAX_STEP = 28
 
# human = True
# cur_candies = CANDIES
 
 
# def get_ai_step():
#     return randint(1, min(MAX_STEP, cur_candies))
 
 
# def get_human_step():
#     while True:
#  cnt = input('Введите количество конфет: ')
#         if cnt.isdigit() and  1 <= int(cnt) <= min(MAX_STEP, cur_candies):
#             ( int(cnt)
#         print('Введено некорректное значение')
 
 
# while cur_candies:
#     if human:
#  cur_candies -= get_human_step()
#     else:
#  cur_candies -= get_ai_step()
#  human = not human
 
# if human:
#     print('Победил БОТ')
# else:
#     print('Победил человек')
