#апишите программу, удаляющую из текста все слова, содержащие ""абв"".
stroka = input().split()
str2 = [i for i in stroka if i.find('абв') != 0]
print(str2)