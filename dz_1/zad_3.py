#Задание 3

enter_num = int(input('Please enter the number: '))
x = 0 #индификатор счётчика
sum = 0

while x < enter_num:
    x = x+1
    sum = sum + int(f'{enter_num}' * x)

input (f"Output: {sum}")