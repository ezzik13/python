# 1.	Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
x = int(input("введите номер четверти: "))
if x < 1 or x > 4:
    print("Введите число от 1 до 4")
elif x == 1:
    print("x > 0 and y > 0")
elif x == 2:
    print("x < 0 and y > 0")
elif x == 3:
    print("x < 0 and y < 0")
elif x == 4:
    print("x > 0 and y < 0")