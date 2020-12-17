import time

class TrafficLight:
    __color = "не горит"
    __code_protection = ([1,2,3], [2,3,1], [3,1,2]) #создаём шифр из допустимых комбинации сигналов
    __real_time_prot = [1,2,3] #шифр который стоит по умолчанию до отработки первого сигнала, но он будет менятся
    __cod_obj = 0
    """зараннее обявил переменную которая будет использоватся в методе,
я чёт не нашёл можно ли локально находу создавать локальные переменные в методе класса или нет """
    
    
    def running(self):
        self.__color = 'КРАСНЫЙ' #замените надпись цвета на любую другую и увидете что выскочит КОТЭСТРОФА
        if self.__code_protection.count(self.c_a_p()): # сравниваю шифр полученный из отработавших сигналов с допустимыми комбинациями
            print('Всё гуд')
        else:
            print('КОТЭСТРОФА') # я наверно тупой но break выдаёт ошибку при сборке, поэтому я хз ка кдругим способом экстренно закрыть программу, я просто выведу надпись
        print(self.__color)
        self.output_time(7)
        
        self.__color = "ЖЁЛТЫЙ"
        if self.__code_protection.count(self.c_a_p()):
            print('Всё гуд')
        else:
            print('КОТЭСТРОФА')
        print(self.__color)
        self.output_time(2)
        
        self.__color = "ЗЕЛЁННЫЙ"
        if self.__code_protection.count(self.c_a_p()):
            print('Всё гуд')
        else:
            print('КОТЭСТРОФА')
        print(self.__color)
        self.output_time(15)
        
    def output_time(self, time_a): #Отсчёт секунд, визуализация отсчёта секунд
        for t in range(time_a):
            print(f'осталось {time_a - t} секунд')
            time.sleep(1)
            
    def c_a_p(self): #присваивание цвету определённый номер
        if self.__color =='КРАСНЫЙ':
            self.__cod_obj = 1
        elif self.__color =='ЖЁЛТЫЙ':
            self.__cod_obj = 2
        elif self.__color =='ЗЕЛЁННЫЙ':
            self.__cod_obj = 3
        else:
            self.__cod_obj = 99
       #создаём шифр из отработавших сигналов по присвоенному цветам номеру
        if self.__cod_obj != self.__real_time_prot[0]:
            self.__real_time_prot[1] = int(self.__real_time_prot[2])
            self.__real_time_prot[2] = int(self.__real_time_prot[0])
            self.__real_time_prot[0] = self.__cod_obj
        return self.__real_time_prot
            
            
svetofor = TrafficLight()
svetofor.running()


