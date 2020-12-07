def int_fun(word):
    word_spl = word.split(' ')
    word_out = ''
    for x in range(len(word_spl)):
        word_out = word_out + " " + word_spl[x].title()
    return word_out

word_imp = input('Введите слово маленькими буквами: ')
word_out = int_fun(word_imp)
print(word_out)
    