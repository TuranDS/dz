#Задача 5

my_reit = [9, 8, 5, 4, 4, 1]

new_element = int(input('Введите новое число которое вы хотите добавить в рейтинг: '))

shet_kol_el = 0
new_my_reit = list()
block = True  # блокировщик для while в 12 строке поторый активируется в 15 строке

for i in range(len(my_reit)): # собирает новый список с добавленным нвоым значением
    while block:
         if new_element > int(my_reit[i]):
            new_my_reit.append(new_element)
            block = False
         break
    new_my_reit.append(my_reit[i])
    
    
output_str = ''

for j in new_my_reit: # сорбираем новую строку для показа данных о значение в одной строке
    output_str = output_str + str(j) + str(', ')
    print(j)
    
print(f'Пользователь ввёл число {new_element}. Результат: ' + output_str)

