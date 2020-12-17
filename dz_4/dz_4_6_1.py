from itertools import count

start = int(input('Введите пожайлуста число с которого начинать список: '))
finish = int(input("Введите пожайлуста число на котором закончится список: "))

# spi = [x for x in count(start) if x < finish] не понимаю почему не работает
spi = []

for x in count(start):
    if x > finish:
        break
    spi.append(x)

print(spi)
    


