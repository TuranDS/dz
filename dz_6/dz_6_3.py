class Worker:
    def __init__(self, name, surname, position, okl, prem):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage' : okl, 'bonus' : prem}

class Position(Worker):
    def get_full_name(self):
        out_mes = 'Полное имя работника: '+ f'{surname}'+ ' ' + f'{name}'
        return out_mes
    def get_total_income(self):
        all_money = str(self._income["wage"] + self._income["bonus"])
        return all_money
    
name = input('Введите пожалуйста имя работника: ')
surname = input('Введите пожалуйста фамилию работника: ')
pos = input ('Введите пожалуйста должность работника: ')
okl = int(input('Введите пожалуйста оклад работника работника: '))
prem = int(input('Введите пожалуйста премию сотрудника: '))

# sotr = Worker(name, surname, pos, okl, prem)
sotr = Position(name, surname, pos, okl, prem)
print(sotr.get_full_name())
print(sotr.get_total_income())


    

    
