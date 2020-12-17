
numbe_1 = int(input('Введите первое число: '))
numbe_2 = int(input("Введите второе число: "))

def del_zero (arg_1, arg_2):
    try:
        otv =  arg_1 / arg_2
    except ZeroDivisionError:
        otv = 0
    return otv
    

out_num = del_zero(numbe_1, numbe_2)

print(f'Ваш ответ: {out_num}')
    

    