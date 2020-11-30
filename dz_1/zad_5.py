costs = int(input('Enter the costs: '))#вводим издержки
proceeds = int(input('Enter the proceeds: '))#вводим выручку

if proceeds > costs:
    print('The firm has a profit')# сообщение что фирма в прибыли
    x = 1;
else:
    print('The firm has a loss')# сообщение что фирма в убытке

if x:
    rent = (proceeds - costs) / proceeds#считаем рентабильность
    print(f'Profitability is assessed - {rent}')
    
    amount_workers = int(input('Enter the number of employees: '))
    profit_worker = int((proceeds - costs) / amount_workers)# считает выручкку на одного работника
    
    print(f'The profit per employee will be {profit_worker}')
    
    
    
    


