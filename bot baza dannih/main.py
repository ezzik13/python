from file_meneger import on_display
from file_meneger import new_str
import os
os.chdir(os.path.dirname(__file__))
from telebot import TeleBot, types
import codecs

TOKEN = '5901572992:AAHqgxQb1WzJwTu04naITwnpc3Z9cId2fd8'

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=''''Введите 1 что б добавить новую запись
Введите 2 для вывода справочника на экран
Введите 3 для добавления записей из Вашего файла
Введите 4 для записи справочника в Ваш файл: ''')

 
# @bot.message_handler(commands=['log'])
# def answer(msg: types.Message):
#     bot.send_message(chat_id=msg.from_user.id, text='Вывожу лог')
 
 
@bot.message_handler()
def answer(msg: types.Message):
 
    text = msg.text
 
    if text == '1':
        bot.register_next_step_handler(msg, answer1)
        bot.send_message(chat_id=msg.from_user.id, text='Введите фамилию, имя, номер телефона, пояснение через пробел')
    elif text == '2':
        bot.register_next_step_handler(msg, answer2)
        bot.send_message(chat_id=msg.from_user.id, text='''Введите 1 для построчного вывода
Введите 2 для вывода запись на 4 строки: ''')
    elif text == '3':
        bot.register_next_step_handler(msg, answer3)
        bot.send_message(chat_id=msg.from_user.id, text='отправьте файл')
    elif text == '4':
        bot.send_document(chat_id=msg.from_user.id,  document=open('tel_book.txt', 'rb'))
        
#  bot.send_document(message.chat.id, open(r'Путь_к_документу/Название_документа.txt, 'rb'))

def answer1(msg):
    fam = list(msg.text.split())
    new_str(fam)
    bot.send_message(chat_id=msg.from_user.id, text=f'строка добавлена в книгу')

def answer2(msg: types.Message):

    text = msg.text

    if text == '1':
        j = ''
        str1 = codecs.open("tel_book.txt", "r", encoding='utf-8').read()
        str1 = list(str1.split('\r\n'))
        for x, y in enumerate(str1):
            str1[x] = list(y.split(';'))
            j = (' '.join(str1[x]))
            bot.send_message(chat_id=msg.from_user.id, text=j)

    elif text == '2':
        str1 = codecs.open("tel_book.txt", "r", encoding='utf-8').read()
        str1 = list(str1.split('\r\n'))
        for x, y in enumerate(str1):
            str1[x] = list(y.split(';'))
        for i in str1:
            # bot.send_message(chat_id=msg.from_user.id, text=f'__________') 
            # for j in i:
            bot.send_message(chat_id=msg.from_user.id, text='\n'.join(i))
            
# @bot.message_handler(content_types=['document'])
def answer3(msg: types.Message):
    filename = msg.document.file_name
    with open(filename, 'wb') as file:
        file.write(bot.download_file(bot.get_file(msg.document.file_id).file_path))
    bot.send_message(chat_id=msg.from_user.id, text='Вывожу логыыыы')

# def on_display1():      # выводит в столбик
#     str1 = codecs.open("tel_book.txt", "r", encoding='utf-8').read()
#     str1 = list(str1.split('\r\n'))
#     for x, y in enumerate(str1):
#         str1[x] = list(y.split(';'))
#     for i in str1:
#         bot.send_message(chat_id=msg.from_user.id, text='...')
#         for j in i:
#             bot.send_message(chat_id=msg.from_user.id, text=j)


# def on_display(number):       # выводит строками
#     j = ''
#     str1 = codecs.open("tel_book.txt", "r", encoding='utf-8').read()
#     str1 = list(str1.split('\r\n'))
#     for x, y in enumerate(str1):
#         str1[x] = list(y.split(';'))
#         j = (' '.join(str1[x]))
#         bot.send_message(chat_id=number, text=j)
        
#     elif text == '2':
#         bot.register_next_step_handler(msg, answer2)
#         bot.send_message(chat_id=msg.from_user.id, text='Введите уменьшаемое и вычитаемое')
#     else:
#         bot.send_message(chat_id=msg.from_user.id, text='Вы прислали: ' + msg.text +', а должны были арифметическое действие')


#     elif f == '2':
#         i = input('''Введите 1 для построчного вывода
# Введите 2 для вывода запись на 4 строки: ''')
#         if i == '1':
#             on_display()
#             input()
#         elif i == '2':
#             on_display1()
#             input()
#     elif f == '3':
#         i = input('''Введите 1 если запись в Вашем файле на 1 строку
# Введите 2 если запись в Вашем файл на 4 строки: ''')
#         if i == '1':
#             import_data()
#         elif i == '2':
#             import_data1()
#     elif f == '4':
#         i = input('''Введите 1 для построчного вывода
# Введите 2 для вывода запись на 4 строки: ''')
#         if i == '1':
#             export_data()
#         elif i == '2':
#             export_data1()
#     else:
#         exit()                                                        
  
bot.polling()