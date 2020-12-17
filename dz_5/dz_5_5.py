import random

# создаём рандомный список
num_list = [random.randint(0, 100) for x in range(random.randint(20, 30))]
# записываем в фаил
f = open('dz_5_5_randomlist.txt', 'w')
for x in num_list:
    f.write(str(x) + ' ')  
f.close()
# из фаила записываем в переменную в виде строки
with open('dz_5_5_randomlist.txt', 'r') as re:
    r_str = str(re.read())

# print(r_str)
#  разделяем по пробелам и удаляем в конце строки пустую ячейку списка
r_str = r_str.split(' ')
r_str.remove('')

summ = 0
# суммируем
for x in r_str:
    summ += int(x)
    
print(summ)
        