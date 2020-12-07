nabor = 0
print('Спец символ для остановки набора чисел "S"')

def summ_list(inp_num_l):
    if not inp_num_l[len(inp_num_l) - 1]:
        inp_num_l = inp_num_l[0 : len(inp_num_l) - 1]
        
    nabor_l = nabor
    for x in range(len(inp_num_l)):
        nabor_l = nabor_l + int(inp_num_l[x])
    return nabor_l







while True:
    inp_num = input('Введите пожалуйста набор чисел через пробел: ')
    
    if inp_num.find('S') >= 0:
        inp_num = inp_num[0 : inp_num.find('S')]
        inp_num = inp_num.split(' ')
        nabor = summ_list(inp_num)
        print('Сумма чисел:', nabor)
        break

    inp_num = inp_num.split(' ')
    nabor = summ_list(inp_num)
    print('Сумма чисел:', nabor)













    