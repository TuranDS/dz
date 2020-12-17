#Задача 4
enter_word = input('Введите пожайлуста несколько слов: ')

enter_word_spis = enter_word.split(" ")
schet_word = 0 #счётчик слов


for i in  enter_word_spis: #пробегаемся по всем словам
    schet_word += 1 
    if len(i) > 10:
        new_word = ('')  #переменная для будущего формирования слова для вывода
        schet_char = 0   #счётчик букв
        for j in i:      #побуквенно собираем слово которое будет не больше 10 букв
               new_word += j
               schet_char += 1
               if schet_char >= 10:
                   break
        print(f"{schet_word}) {new_word}")
    else:
        print(f"{schet_word}) {i}")

