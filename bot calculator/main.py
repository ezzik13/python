from telebot import TeleBot, types
import os
os.chdir(os.path.dirname(__file__))
import codecs
import datetime
TOKEN = '5901572992:AAHqgxQb1WzJwTu04naITwnpc3Z9cId2fd8'

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='''Введите 1 для работы с рациональными числами
Введите 2 для работы с комплексными числами''', )

@bot.message_handler()
def answer(msg: types.Message): 
    
    text = msg.text
    with codecs.open("log", "a", encoding='utf-8') as file1:
            file1.writelines(f'\n{text, msg.from_user.id, datetime.datetime.now()}')
 
    if text == '1':
        bot.register_next_step_handler(msg, float_calc)
        bot.send_message(chat_id=msg.from_user.id, text='Введите выражение с пробелами между числами и знаками')
    elif text == '2':
        bot.register_next_step_handler(msg, compl_calc)
        bot.send_message(chat_id=msg.from_user.id, text='Введите выражение с пробелами между числами и знаками, но без пробелов внутри комплексного числа')

 
@bot.message_handler()
def float_calc(msg: types.Message):
 
    lst = list(msg.text.split())

    with codecs.open("log", "a", encoding='utf-8') as file1:
            file1.writelines(f'\n{lst, msg.from_user.id, datetime.datetime.now()}')

    if lst[1] == '+':
        bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {float(lst[0]) + float(lst[2])}')
    elif lst[1] == '-':
        bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {float(lst[0]) - float(lst[2])}')
    elif lst[1] == '*':
        bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {float(lst[0]) * float(lst[2])}')
    elif lst[1] == '/':
        if lst[2] == '0':
            bot.send_message(chat_id=msg.from_user.id, text="деление на 0 недопустимо")
            os._exit()
        bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {float(lst[0]) / float(lst[2])}')
    
    else:
        bot.send_message(chat_id=msg.from_user.id, text='Вы прислали: ' + msg.text +', а должны были "число, пробел, знак действия, пробел, число"')

bot.message_handler()                                                        
def compl_calc(msg: types.Message):

    lst = list(msg.text.split())

    with codecs.open("log", "a", encoding='utf-8') as file1:
            file1.writelines(f'\n{lst, msg.from_user.id, datetime.datetime.now()}')
    
    if lst[2] == '0' and lst[1] == '/':
        bot.send_message(chat_id=msg.from_user.id, text="деление на 0 недопустимо")
    
    for i in lst[0]:
        if '+' or '-' in i:
            a_complex = complex(lst[0])
            break
        if '+' or '-' not in i:
            a_complex = f'0+{lst[0]}'
            complex(a_complex)

    for i in lst[2]:
        if '+' or '-' in i:
            b_complex = complex(lst[2])
            break
        if '+' or '-' not in i:
            b_complex = f'0+{lst[2]}'
            complex(b_complex)
    
    if lst[1] == '+':
        result = str(a_complex + b_complex)
        if '1j' in result:
            result.replace('1j','j')
        bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {result}')
    if lst[1] == '-':
        result = str(a_complex - b_complex)
        if '1j' in result:
            result.replace('1j','j')
        bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {result}')
    if lst[1] == '*':
        result = str(a_complex * b_complex)
        if '1j' in result:
            result.replace('1j','j')
        bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {result}')
    if lst[1] == '/':
        result = str(a_complex / b_complex)
        if '1j' in result:
            result.replace('1j','j')
        bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {result}')





# @bot.message_handler(commands=['log'])
# def answer(msg: types.Message):
#     bot.send_message(chat_id=msg.from_user.id, text='Вывожу лог')
  
bot.polling()