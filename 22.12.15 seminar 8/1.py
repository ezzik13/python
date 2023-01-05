# Создать информационную систему позволяющую работать с сотрудниками некой компании
#  \ студентами вуза \ учениками школы.
lst_ = list(input('введите выражение: ').split())

def calc(lst):
    if lst[1] == '+':
        print(f'Результат сложения {float(lst[0]) + float(lst[2])}')
    elif lst[1] == '-':
        print(f'Результат вычитания {float(lst[0]) - float(lst[2])}')
    elif lst[1] == '*':
        print(f'Результат умноожения {float(lst[0]) * float(lst[2])}')
    elif lst[1] == '/':
        if lst[2] == '0':
            print("деление на 0!")
while True:
    calc(lst_)
    lst_ = list(input('введите выражение: ').split())
    if lst_[0] == 'q':
        break