import random
class Car:
    def __init__(self, color, name, is_police, turn_s = 'Прямо'):
        self.speed = random.randint(10,90)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
        self.turn_s = turn_s
    
    def go(self):
        print('Вы поехали')
        self.speed = random.randint(10,90)
    def stop(self):
        self.speed = 0
        print('Вы стоите на месте')
    def turn(self, turn_s):
        self.turn_s = turn_s
        print('Вы повернули на ', turn_s)
    def show_speed(self):
        print('Ваша скорость на данный момент: ', self.speed)
    def status(self):
        print('На данынй момент ваша скорость - ',self.speed)
        print('Цвет машины - ',self.color)
        print('Ваше ведро вы зовёте - ', self.name)
        print('Машина развёрнута ', self.turn_s)
        if self.is_police:
            print('Вы являетесь полицейским')
            print('Ля ты крыса...')

class TownCar(Car):
    def show_speed(self):
        print('Ваша скорость на данный момент: ', self.speed)
        if self.speed > 60:
            print('АХТУНГ! Вы привысили допустимую отметку скорости в 60 км\ч.')
    
class SportCar(Car):
    def show_speed(self):
        print('Ваша скорость на данный момент: ', self.speed)
        if self.speed > 40:
            print('АХТУНГ! Вы привысили допустимую отметку скорости в 40 км\ч.')
    
class WorkCar(Car):
    pass
class PoliceCar(Car):
    pass
my_car = TownCar('Красная','Красная жемчужина', True, 'В сторону церкви')
my_car.status()
my_car.turn('дальний дальний север')
sup_driver = SportCar('серебристая','Пуля', False)
sup_driver.stop()
sup_driver.show_speed()
sup_driver.go()
sup_driver.show_speed()
sup_driver.turn('НА ИЕРУСАЛИМ')
sup_driver.status()
my_car.go()
my_car.show_speed()