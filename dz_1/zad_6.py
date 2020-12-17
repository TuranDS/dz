a = int(input('Enter the distance on the first day: '))
b = int(input('enter the result distance: '))

i_d = 1 #счётчик дней
w_d = a #дистанция для счётчика
print(f'{i_d} day: {a}') 

if a > b:
    print(f'On the {i_d}th day the smortsman reached the {b} km mark')
else:
    while w_d < b:    
        w_d = w_d * 1.1
        i_d = i_d + 1
        print(f'{i_d} day: {round(w_d, 2)}')

    print(f'On the {i_d}th day the smortsman reached the {b} km mark')

    
    

    
