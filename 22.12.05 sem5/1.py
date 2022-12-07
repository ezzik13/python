# past_el = None

# with open('text.txt') as f:
#     for item in map(int, f.read().split( )):
#         if past_el is None:
#             past_el = item
#         else:
#             if item != past_el + 1:
#                 print(past_el + 1)
#             past_el = item
# 
                
with open("files/test", "r") as data:
    lst = list(map(int, data.read().split()))

res = 0
for key, item in enumerate(lst):
    if key + 1 < len(lst) and item + 1 != lst[key + 1]:
        res = item + 1
   
print(res)
