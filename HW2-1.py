#напишите программу, удаляющую из текста все слова, содержащие ""абв"".
stroka = input().split()
str2 = list(filter(lambda x: x.find('абв') !=0, stroka))
print(str2)
