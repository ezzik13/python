# 5 Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint
import random

lst = [1, 2, 3, 4, 5]
j = 0
for i in range(len(lst)):
    j = random.randint(1, len(lst)-1)
    lst[i], lst[j] = lst[j], lst[i]

print(lst)