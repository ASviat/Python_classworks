#Напишите прогу, принимающую два числа и проверяющую, является ли одно квадратом другого.

num_first=int(input ("Введите число 1: "))
num_second=int(input("Введите число 2: "))

if num_first*num_first==num_second:
    print ('Второе число является квадратом первого')

elif num_second*num_second==num_first:
    print('Первое является квадратом второго')
else:
    print('Мавр ошибся.')