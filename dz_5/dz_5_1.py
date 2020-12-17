
cont = []
while True:
    cont.append(input('Введите строку для записи: ') + '\n')
    if cont[-1] == "\n":
        cont = cont[:-1]
        break

with open("dz_5_1_cont.txt", "w") as w_str:
    w_str.writelines(cont)
    
