# 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

# aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
# 4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff

import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

str1 = open("files/f2 for l5.txt", "r").read()
print(str1)
def f(x: str):
    res = ''
    count = 1
    for i in range(1, len(x)-1):
        if x[i] == x[i-1]:
            count += 1
        else:
            while count > 9:
                res = res + '9' + x[i-1]
                count -= 9
            res = res + (f'{count}') + x[i-1]
            count = 1
    if x[-1] == x[-2]:
        while count > 9:
                res = res + '9' + x[i-1]
                count -= 9
        res = res + (f'{count}') + x[i-1]
    else:
        res = res + '1' + x[-1]
    return res

str2 = f(str1)

print(str2)

with open("files/f3 for l5.txt", "w") as file1:
    file1.writelines(str2)

str3 = ''

for i, item in enumerate(str2):
    if item.isdigit():
        str3 = str3 + int(item) * str2[i+1]

print(str3)

with open("files/f3 for l5.txt", "a") as file1:
    file1.writelines(f'\n{str3}')

