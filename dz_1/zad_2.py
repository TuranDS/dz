#Задание 2

ent_time_sec = int(input('Please enter time in second: '))

time_1_hour_per_sec = 60*60 #секунд в одном часе
time_1_min_per_sec = 60 #секунд в минуте

int_real_hour = ent_time_sec // time_1_hour_per_sec # количество часов
after_poin_hour = ent_time_sec % time_1_hour_per_sec # остаток от часов
int_real_minute = after_poin_hour // time_1_min_per_sec # количество минут
int_real_sec = after_poin_hour % time_1_min_per_sec # количество секунд

print(f'Введённые вами секунды в формате времени: {int_real_hour}:{int_real_minute}:{int_real_sec}')