import os
os.chdir(os.path.dirname(__file__))
import codecs
# str1 = codecs.open("tel_book.txt", "r", encoding='utf-8').read()
# print(str1)


def new_str(a: list):     # добавляет новую строку с консоли
    with open("tel_book.txt", "a", encoding='utf-8') as file1:
        file1.writelines(f'\n{";".join(a)}')

def on_display():       # выводит строками
    str1 = codecs.open("tel_book.txt", "r", encoding='utf-8').read()
    str1 = list(str1.split('\r\n'))
    for x, y in enumerate(str1):
        str1[x] = list(y.split(';'))
        print(' '.join(str1[x]))
        

def on_display1():      # выводит в столбик
    str1 = codecs.open("tel_book.txt", "r", encoding='utf-8').read()
    str1 = list(str1.split('\r\n'))
    for x, y in enumerate(str1):
        str1[x] = list(y.split(';'))
    for i in str1:
        for j in i:
            print(j)
        print()

def import_data(data_file1):    
    new_lst = codecs.open(f'{data_file1}', "r", encoding='utf-8').read()
    new_lst = list(new_lst.split('\r\n'))
    for x, y in enumerate(new_lst):
        new_lst[x] = list(y.split(';'))
    for x, y in enumerate(new_lst):
        with open("tel_book.txt", "a", encoding='utf-8') as file1:
            file1.writelines(f'\n{";".join(new_lst[x])}')
def import_data1():
    data_file1 = input('Введите наименование файла с расширением: ')
    new_lst = codecs.open(f'{data_file1}', "r", encoding='utf-8').read()
    new_lst = list(new_lst.split('\r\n'))
   
    new_lst_1 = []
    new_str = ''
    for x, y in enumerate(new_lst):
        if y != '':
            if x > 0:
                if new_lst[x-1] != '':
                    new_str += ';'
            new_str += y
        if y == '' or x+1 == len(new_lst):
            new_lst_1.append(f'{new_str}')
            new_str = ''
    for x in new_lst_1:
        with open("tel_book.txt", "a", encoding='utf-8') as file1:
            file1.writelines(f'\n{x}')

def export_data():
    data_file1 = input('Введите наименование файла: ')
    new_lst = codecs.open("tel_book.txt", "r", encoding='utf-8').read()
    new_lst = list(new_lst.split('\r\n'))
    for x, y in enumerate(new_lst):
        new_lst[x] = list(y.split(';'))
    for x, y in enumerate(new_lst):
        with open(f'{data_file1}', "a", encoding='utf-8') as file1:
            file1.writelines(f'{" ".join(new_lst[x])}\n')

def export_data1():
    data_file1 = input('Введите наименование файла: ')
    new_lst = codecs.open("tel_book.txt", "r", encoding='utf-8').read()
    new_lst = list(new_lst.split('\r\n'))
    for x, y in enumerate(new_lst):
        new_lst[x] = list(y.split(';'))
    for i in new_lst:
        for j in i:
            with open(f'{data_file1}', "a", encoding='utf-8') as file1:
                file1.writelines(f'{j}\n')
        with open(f'{data_file1}', "a", encoding='utf-8') as file1:
            file1.writelines('\n')
