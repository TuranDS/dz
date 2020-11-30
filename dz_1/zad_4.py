#Задание 4

enter_num = input('Please enter the number: ')

len_str = len(enter_num)#узнаём длину строки
max_res = 0 #максимально большая цифра найденная в строке
i  = 0 #счётчик для цикла

while i < len_str:
    if int(enter_num[i]) > int(max_res):
        max_res = enter_num[i]
    i = i + 1

print(max_res)