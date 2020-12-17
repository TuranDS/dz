r_f = open('dz_5_6_content.txt', 'r')
r_f_s = r_f.readlines()
r_f.close()

stat = {}

for pred in (r_f_s):
    name_dist = pred[ : pred.find(':')] #делю строку на 2 части чтобы поиск цифр не проходил в названии предмета
    two_part = pred[pred.find(':')+1 : ]
# и тут я узнал про .isdigit().....
# до этого я искал циферки исключением...
    sum_line = 0
    s_l_str = str()
    for char in two_part:
        if char.isdigit():
            s_l_str += char
        else:
            if s_l_str:
                sum_line += int(s_l_str)
                s_l_str = str()
    stat[name_dist] = sum_line
print(stat)
            



#     
#     summ = 0
#     
#     for split_str in two_part.split(' '):
#         if split_str != '' and split_str != '-':
#             print(list(split_str))
#             
#             n_t = str()       
#             for char in split_str:
#                 if char != '-':
#                     print(char)
#                     try:                         # нахождения чисел исключением 
#                         n = int(char)
#                         n_t = n_t + char
#                     except ValueError:
#                         continue
#             print(n_t)
#             summ += int(n_t)
#     stat[name_dist] = summ
#         
#     print(n_t)
    

        
    

