from file_meneger import import_data
from file_meneger import import_data1
from file_meneger import on_display1
from file_meneger import on_display
from file_meneger import new_str
from file_meneger import export_data
from file_meneger import export_data1

def my_interface():
    f = input('''Введите 1 что б добавить новую запись
Введите 2 для вывода справочника на экран
Введите 3 для добавления записей из Вашего файла
Введите 4 для записи справочника в Ваш файл: ''')
    if f == '1':
        new_str()
    elif f == '2':
        i = input('''Введите 1 для построчного вывода
Введите 2 для вывода запись на 4 строки: ''')
        if i == '1':
            on_display()
            input()
        elif i == '2':
            on_display1()
            input()
    elif f == '3':
        i = input('''Введите 1 если запись в Вашем файле на 1 строку
Введите 2 если запись в Вашем файл на 4 строки: ''')
        if i == '1':
            import_data()
        elif i == '2':
            import_data1()
    elif f == '4':
        i = input('''Введите 1 для построчного вывода
Введите 2 для вывода запись на 4 строки: ''')
        if i == '1':
            export_data()
        elif i == '2':
            export_data1()
    else:
        exit()

    
my_interface()