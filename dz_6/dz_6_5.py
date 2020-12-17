import random
class Stationary:
    def __init__(self, title_i):
        self.title = title_i
    def draw(self):
        print('Запуск отрисовки')
        
class Pen(Stationary):
    def draw(self):
        print('Запуск отрисовки ручкой')
class Pencil(Stationary):
    def draw(self):
        print('Запуск отрисовки карандашом')
class Handle(Stationary):
    def draw(self):
        print('Запуск отрисовки маркером')
        
worker_hand = Handle('Стрёмный найденный на паре маркер')
worker_hand.draw()
    
long_tree = Pencil('Карандаш из красного дерева и алмаза')
long_tree.draw()

my_red_hand = Pen('Моя рука испачканная кровью от бесконечной игры HoM_5')
my_red_hand.draw()
        
