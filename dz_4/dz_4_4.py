import random

len_spi = int(input('Введите длину списка: '))
max_random = int(input("Введите максимальное число в вашем списке: "))

start_spi = [random.randint(1, max_random) for x in range(0, len_spi)]

print(start_spi)

# решение без генератора
# work_spi = list()
# for x in start_spi:
#     if start_spi.count(x) == 1:
#         work_spi.append(x)
#         
# print(work_spi)

work_spi =  [y for y in start_spi if start_spi.count(y) == 1]

print(work_spi)
