# 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*

# - 6782 -> 23
# - 0.56 -> 11

number = (input("введите число: "))

number = number.replace('.', '')

sum = 0

for i in range(len(number)):
    sum = sum + int(number[i])
        

print(f"сумма цифр введенного числа = {sum} ")