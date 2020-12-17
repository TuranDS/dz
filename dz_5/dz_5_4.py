new_cont = []

with open('dz_5_4_content.txt') as input_cont:
    for line in input_cont:
        new_cont.append(line.split(' '))
        

for lins in range(len(new_cont)):
    for word in new_cont[lins]:
        if word == 'One':
            new_cont[lins][0] = 'Один'
        elif word == 'Two':
            new_cont[lins][0] = 'Два'
        elif word == 'Three':
            new_cont[lins][0] = 'Три'
        elif word == 'Four':
            new_cont[lins][0] = 'Четыре'
            


with open('dz_5_4_new_content.txt', 'w') as output_cont:
    for line in new_cont:
        output_cont.write(str(line[0]) + ' ' + str(line[1]) + ' ' + str(line[2]))