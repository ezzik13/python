import datetime
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()
def time1():
    return (datetime.datetime.now().microsecond // 100 % 10) **\
        (datetime.datetime.now().microsecond % 10)

cls()
print(time1())





