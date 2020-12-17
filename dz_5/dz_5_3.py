zp_file = open('dz_5_3_cont.txt', 'r')
dict_zp = {}
amount_worker = 0

for line in zp_file:
    line = line.split(' ')
    zp = str()
    
    for char in line[-1]:
        try:                         # нахождения чисел исключением 
            p = int(char)
            zp = zp + char
        except ValueError:
            continue
    if zp:
        
        dict_zp[line[0]] = zp
        
    amount_worker += 1 #cчётчик работников

i_m_z = 0 #всего денег
for i in dict_zp:
    i_m_z += int(dict_zp[i])
    
m_z = i_m_z / amount_worker    


        
for x in dict_zp:
    print(x, dict_zp[x])
print(f"Средняя зарплата на работника состовляет - {round(m_z)} средиземских условных едениц")

#в списке работников есть сущности которые работают на недоступной смертным мотивацию

zp_file.close()

        
    