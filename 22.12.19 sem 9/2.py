from telebot import TeleBot, types

TOKEN = '5901572992:AAHqgxQb1WzJwTu04naITwnpc3Z9cId2fd8'

bot = TeleBot(TOKEN)

# @bot.message_handler()
# def answer(msg: types.Message):
#     bot.send_message(chat_id=msg.from_user.id, text='Вы прислали: ' + msg.text)

# bot.polling()

# @bot.message_handler()
# def answer(msg: types.Message):
 
#  text = msg.text
 
#     ( int(text) % 2 == 0:
#  bot.register_next_step_handler(msg, answer1)
#     else:
#  bot.register_next_step_handler(msg, answer2)
 
#  bot.send_message(chat_id=msg.from_user.id, text='Вы прислали: ' + msg.text)
 
 
# def answer1(msg):
#  bot.send_message(chat_id=msg.from_user.id, text='Вы ввели чётное число')
 
 
# def answer2(msg):
#  bot.send_message(chat_id=msg.from_user.id, text='Вы ввели нечётное число')

@bot.message_handler(commands=['start', 'help'])
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='Вывожу команды', )
 
 
# @bot.message_handler(commands=['log'])
# def answer(msg: types.Message):
#     bot.send_message(chat_id=msg.from_user.id, text='Вывожу лог')
 
 
@bot.message_handler()
def answer(msg: types.Message):
 
    text = msg.text
 
    if text == '+':
        bot.register_next_step_handler(msg, answer1)
        bot.send_message(chat_id=msg.from_user.id, text='Введите слагаемые')
    elif text == '-':
        bot.register_next_step_handler(msg, answer2)
        bot.send_message(chat_id=msg.from_user.id, text='Введите уменьшаемое и вычитаемое')
    else:
        bot.send_message(chat_id=msg.from_user.id, text='Вы прислали: ' + msg.text +', а должны были арифметическое действие')
                                                        
 
 
def answer1(msg):
    a, b = map(int, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат сложения {a + b}')
 
 
def answer2(msg):
    a, b = map(int, msg.text.split())
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат вычитания {a - b}')
 
 
bot.polling()