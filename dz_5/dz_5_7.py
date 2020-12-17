import json
cont_firm = open('dz_5_7_content.txt', 'r')
count_middle_prof = 0
sum_prof = 0
itog_d = dict()

for line in cont_firm:
    line = line.strip(' ')
    line = line.strip('\n')
    line_s = line.split(' ')
    itog_d[line_s[0]] = int(line_s[2]) - int(line_s[3])
    if itog_d[line_s[0]] > 0:
        count_middle_prof += 1
        sum_prof += itog_d[line_s[0]]
prof = {'average_prof' : round(sum_prof / count_middle_prof)}

result = [itog_d, prof]

cont_firm.close()

with open('dz_7_data.json', 'w') as py_js:
    json.dump(result, py_js)
