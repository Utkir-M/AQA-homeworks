#def month_to_season(n):
#    if (n > 0) and (n < 3) or (n == 12): 
#        print("Зима")
#    elif (n > 2) and (n < 6):
#        print('Весна')
#    elif (n > 5) and (n < 9):
#        print('Лето')
#    elif (n > 8) and (n < 12):
#        print('Осень')
#    else:
#        print('Такого месяца не существует')

#month_to_season(int(input('Введите номер месяц >>> ')))

#Более простое решение
def month_to_seasons(seasons):
    if seasons in [1, 2, 12]:
        print('Зима')
    elif seasons in [3, 4, 5]:
        print('Весна')
    elif seasons in [6, 7, 8]:
        print('Лето')
    elif seasons in [9, 10, 11]:
        print('Осень')
    else:
        print('Такого месяца не существует') 

month_to_seasons(int(input('Введите номер месяц >>> ')))

#Научиться пользоваться оператором 'while'