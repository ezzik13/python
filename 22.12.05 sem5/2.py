txt = 'Привет, заБвение меня накрыло, этот опыт был незабвен и я не был пьян'
print(f"Исходный текст: {txt}")
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i.lower()]
print(f'Результат: {" ".join(lst)}')
