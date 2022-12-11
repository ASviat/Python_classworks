# Принимает дробное, возвращает первую цифру после запятой

numb = float(input('Введите дробное число: '))
numb = int(numb*10 % 10)
if numb > 0:
    print(numb)
else:
    print('Нет')
