work_file = open('dz_5_2_cont.txt', 'r')
amo_words = 0
amo_lines = 0
for a_l in work_file:
    if a_l != '\n':
        amo_lines += 1
    for a_w in a_l.split(' '):
        amo_words += 1

print(f'Количество строк в фаиле - {amo_lines} \b Количество слов в фаиле - {amo_words}')

work_file.close()