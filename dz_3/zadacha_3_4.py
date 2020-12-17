
x = input('Введите действительно число: ')
y = input('Введите отрицательное число: ')

try:
    x = float(x)
    y = int(y)
    
except ValueError:
    x = int(x)
    y = float(y)


# вариант с **

def my_func(artorius, drevn):
    if type(artorius) == float:
        drevn = abs(drevn)
        l = int(artorius ** drevn)
    else:
        artorius = abs(artorius)
        l = int(drevn ** artorius)
    return l

print(f'Ответ с **: {my_func(x, y)}')

# вариант БЕЗ **
def my_func(artorius, drevn):
    if type(artorius) == float:
        art_step = artorius
        drevn = abs(drevn)
        for s in range(1, drevn, 1):
            artorius *= art_step
        l = int(artorius)
    else:
        dre_step = drevn
        artorius = abs(artorius)
        for s in range(1, artorius, 1):
            drevn *= dre_step
        l = int(drevn)
    return l

print(f'Ответ варианта БЕЗ **: {my_func(x, y)}')
    
    