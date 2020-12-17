#задача 3
#решение через словари

winter = {12:12, 1:1,2:2}
spring = {3:3, 4:4, 5:5}
summer = {6:6, 7:7, 8:8}
autumn = {9:9, 10:10, 11:11}

seasons = {1: winter, 2: spring, 3: summer,4: autumn}

while True:
    enter_num = int(input('Введите число от 1 до 12: '))
    if enter_num < 12:
        break
    
for i in seasons:
    for j in seasons.get(i):
        if enter_num == j:
            if seasons.get(i) == winter:
                print('ЗИМА')
            elif seasons.get(i) == spring:
                print('ВЕСНА')
            elif seasons.get(i) == summer:
                print('ЛЕТО')
            elif seasons.get(i) == autumn:
                print('ОСЕНЬ')