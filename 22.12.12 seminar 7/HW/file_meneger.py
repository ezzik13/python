import os
os.chdir(os.path.dirname(__file__))
import codecs
# str1 = codecs.open("tel_book.txt", "r", encoding='utf-8').read()
# print(str1)


def new_str():     # добавляет новую строку с консоли
    n_str = []
    n_str.append(input('Введите фамилию: '))
    n_str.append(input('Введите имя: '))
    n_str.append(input('Введите телефон: '))
    n_str.append(input('Введите пояснение: '+'\n'))
    with open("tel_book.txt", "a", encoding='utf-8') as file1:
        file1.writelines(f'\n{";".join(n_str)}')

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

def import_data():
    data_file1 = input('Введите наименование файла с расширением: ')
    new_lst = codecs.open(f'{data_file1}', "r", encoding='utf-8').read()
    new_lst = list(new_lst.split('\r\n'))
    for x, y in enumerate(new_lst):
        new_lst[x] = list(y.split(';'))
    for x, y in enumerate(new_lst):
        with open("tel_book.txt", "a", encoding='utf-8') as file1:
            file1.writelines(f'\n{";".join(new_lst[x])}')

def export_data():
    data_file1 = input('Введите наименование файла: ')
    new_lst = codecs.open("tel_book.txt", "r", encoding='utf-8').read()
    new_lst = list(new_lst.split('\r\n'))
    for x, y in enumerate(new_lst):
        new_lst[x] = list(y.split(';'))
    for x, y in enumerate(new_lst):
        with open(f'{data_file1}', "a", encoding='utf-8') as file1:
            file1.writelines(f'{" ".join(new_lst[x])}\n')



