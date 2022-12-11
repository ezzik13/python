# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*      
# 2+2 => 4;     
# 7-8+3*5+1+1+2*3 => 22;  
# a = '7-82+3*5+13+1+25*3'  
# b = ['7', '-', '82', '+', '3', '*', '5', '+', '13', '+', '1', '+', '25', '*', '3']
# 7, -8, 15, 1, 1, 6
# 1-2*3 => -5;
str_ = '10+5*1-50+6'
lst = []
last = -1

for i, symbol in enumerate(str_):
    if not symbol.isdigit():
        lst.append(int(str_[last + 1:i]))
        lst.append(symbol)
        last = i
    # print(i, symbol, lst, last)

lst.append(int(str_[last + 1:i + 1]))
print(lst)

lst_1 = []
if type(lst[0]) is int:
    lst_1.append(lst[0]) 

for i, symbol in enumerate(lst):
    if symbol == "*":
        lst_1[-1] = lst_1[-1] * lst[i + 1]
    elif symbol == "/":
        lst_1[-1] = lst_1[-1] / lst[i + 1]
    elif symbol == "+":
        lst_1.append(lst[i + 1])
    elif symbol == "-":
        lst_1.append(-lst[i + 1])

print(sum(lst_1))
