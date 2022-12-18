from ui import my_interface
import os

while True:
    os.system('cls||clear')
    my_interface()
    is_continue = input("Продлжить - press Enter,  Завершить работу - exit: ")
    if is_continue == "exit":
        break