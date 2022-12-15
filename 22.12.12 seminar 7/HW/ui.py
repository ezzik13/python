from file_meneger import import_data
from file_meneger import on_display1
from file_meneger import on_display
from file_meneger import new_str
from file_meneger import export_data 

def my_interface():
    f = int(input('''Введите 1 что б добавить новую запись
Введите 2 для вывода справочника на экран
Введите 3 для добавления записей из Вашего файла
Введите 4 для записи справочника в Ваш файл: '''))
    if f == 1:
        new_str()
    elif f == 2:
        i = int(input('''Введите 1 для построчного вывода
Введите 2 для вывода запись на 4 строки: '''))
        if i == 1:
            on_display()
        elif i == 2:
            on_display1()
    elif f == 3:
        import_data()
    elif f == 4:
        export_data()
    
my_interface()