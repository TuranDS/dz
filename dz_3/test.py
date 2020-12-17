num_1 = int(input('Введите число 1: '))
num_2 = int(input('Введите число 2: '))
num_3 = int(input('Введите число 3: '))

def old_hroft(tor, loki, fenrir ):
    a = max([tor, loki, fenrir])
    list_1 = [tor,loki, fenrir]
    list_1.remove(a)
    print(list_1)
    
old_hroft(num_1, num_2, num_3)
    
 