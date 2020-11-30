#задача 3

#решение через списки
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

seasons = [winter, spring, summer, autumn]



while True:
    enter_num = int(input('Введите число от 1 до 12: '))
    if enter_num < 12:
        break
    
for i in range(len(seasons)):
    for j in range(len(seasons[i])):
        if enter_num == seasons[i][j]:
            if seasons[i] == [12, 1, 2]:
                print ('Это зима')
            elif seasons[i] == [3, 4, 5]:
                print ('Это весна')
            elif seasons[i] == [6, 7, 8]:
                print ('Это лето')
            elif seasons[i] == [9, 10, 11]:
                print ('Это осень')
  