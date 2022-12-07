# Дан список чисел. Создайте список, в который попадают числа, описываемые   возрастающую последовательность. Порядок элементов менять нельзя. 
#      *Пример:*      
#      [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
lst = [1, 5, 2, 3, 4, 6, 1, 7]
lst1 = [lst[0]]
for i in lst:
    if i > lst1[-1]:
        lst1.append(i)
print(lst1)


# array = [1, 5, 2, 3, 4, 6, 1, 7]

# for i in range(len(array)):
#     arr_n = [1]
#     arr_n[0] = array[0]
#     for j in range(i, len(array)):
#         if array[j] > arr_n[-1]:
#             arr_n.append(array[j])

#     print(arr_n)
