# 2.	Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = float(input("введите координату Х первой точки: "))
y1 = float(input("введите координату Y первой точки: "))
x2 = float(input("введите координату Х второй точки: "))
y2 = float(input("введите координату Y второй точки: "))
s = ((x2 - x1) ** 2 + (y2 -y1) ** 2) ** 0.5
print(round(s, 2))