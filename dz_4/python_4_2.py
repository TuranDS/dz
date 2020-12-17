import random

len_spi = int(input('Введите длину списка: '))
max_random = int(input("Введите максимальное число в вашем списке: "))

spi = [random.randint(1, max_random) for x in range(0, len_spi)]

# Альтернативное решение:
# for x in range(0, len_spi):
#     spi.append(random.randint(1, max_random))


#Так как первое число не стоит перед каким либо значением то его не будем сравнивать с предыдущим

out_spi = []

for x in range(1, len(spi)):
    if spi[x] > spi[x - 1] :
        out_spi.append(spi[x])
        
print("Сгенерированный список: ", spi)
print("Список прошедший скрипт: ",out_spi)
    


