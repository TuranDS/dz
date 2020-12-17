num_1 = int(input('Введите число 1: '))
num_2 = int(input('Введите число 2: '))
num_3 = int(input('Введите число 3: '))

def old_hroft(tor, loki, fenrir ):
    a = max([tor, loki, fenrir])
    list_1 = [tor,loki, fenrir]# почему я не могу в объявление списка сразу добавить метод ремов?
    list_1.remove(a)
    if list_1[0] > list_1[1]:
        b = list_1[0]
    else:
        b = list_1[1]
    return a,b
    
print(old_hroft(num_1, num_2, num_3))
