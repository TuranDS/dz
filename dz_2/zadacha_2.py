#Задача 2
spis = list()
while 1:
        add_el = input('Введите элемент который хотите добавить в список :')
        spis.append(add_el)
        command = input('Если вы закончили введите "STOP", для продолжения жмите ENTER: ')
        if command == "STOP":
            break
metka = 0

if len(spis) % 2 > 0:                     # проверяем количество элементов на чётность, и если оно не чётное то вырезаем и записываем в отдельюную переменную
    pos_el = spis[len(spis) - 1]
    spis.pop(len(spis) - 1)
    metka = 1                             # ставим меку которая пригодится для форматирования финального списка

spis_1 = list()
i = 0

while i < len(spis):                      # записываем в новый список поменянные значения из старого
    spis_1.append(spis[i + 1])
    spis_1.append(spis[i])
    i = i + 2
if metka == 1:                            # используем метку чтобы решить надо добавлять значение в конце или нет
    spis_1.append(pos_el)

print(spis_1)