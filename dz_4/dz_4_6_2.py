import random
from itertools import cycle

len_spi = int(input('Введите длину списка: '))
max_random = int(input("Введите максимальное число в вашем списке: "))

start_spi = [random.randint(1, max_random) for x in range(0, len_spi)]

print("Cгенерируемый начальный спсиок: ", start_spi)

count = 0
fin_spi = []

for x in cycle(start_spi):
    count += 1
    if count > len(start_spi):
        break
    fin_spi.append(x)
    
print('Скопированный список: ',fin_spi)
    




