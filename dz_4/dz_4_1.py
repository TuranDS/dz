from sys import argv

scr_name, work_hour, stavka_hour, prem = argv

zp = (int(work_hour) * int(stavka_hour)) + int(prem)

print("Зарплата состовляет - ", zp)