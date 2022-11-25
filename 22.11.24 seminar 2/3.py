# Напишите программу, в которой пользователь будет задавать две строки, 
#    а программа - определять количество вхождений одной строки в другой.

# s1 = 'aaababaewfwef'
# s2 = 'aba'

# print(s1.count(s2))
# '''

str1 = input("введите строку 1 : ")
str2 = input("введите строку 2 : ")
count = 0
for i  in range(len(str1) - (len(str2)-1)):
    if str2 == str1[i:i+len(str2)]:
        count += 1
        

print(count)
