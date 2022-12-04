# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

with open('file1.txt', 'r') as data:
    for line in data:
        str1 = line.split(' + ')

for i in range(len(str1)):
    str1[i] =  str1[i].split()

str1[len(str1)-1].remove('=')
str1[len(str1)-1].remove('0')

print(str1)

with open('file2.txt', 'r') as data:
    for line1 in data:
        str2 = line1.split(' + ')

for i in range(len(str2)):
    str2[i] =  str2[i].split()

str2[len(str2)-1].remove('=')
str2[len(str2)-1].remove('0')

print(str2)

for i in str1:
    for j in str2:
        i[0] = int(i[0])
        j[0] = int(j[0])
        if i[-1] == j[-1]:
            i[0] = i[0]+ j[0]
            str2.remove(j)
        elif len(i) == len(j) == 1:
            i[0] = i[0] + j[0]
            str2.remove(j)

str1.append(*str2)
        
with open('file3.txt', 'w') as data:
    data.write('')
for i in range(len(str1)-1):
    str1[i].append(" + ")
print(str1)

for i in str1:
    with open('file3.txt', 'a') as data:
        data.write(" ".join(map(str,i)))
with open('file3.txt', 'a') as data:
        data.write(" = 0")       