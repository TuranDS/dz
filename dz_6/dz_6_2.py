class Road:
    def __init__(self,lenght = 0, width = 0):
        self._lenght = lenght
        self._width = width
        
    def calculation(self):
        thickness = 5
        weight_1_m = 25
        return self._lenght * self._width * thickness * weight_1_m
        
 
l = int(input('Введте длину дороги: '))
w = int(input('Введте ширину дороги: '))

my_road = Road(l, w)
print('Масса вашей дороги ровна: ', int(my_road.calculation()), 'т')