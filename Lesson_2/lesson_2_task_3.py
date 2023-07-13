import math

def square(side):
    side = math.ceil(float(side))
    print('Площадь квадрата =', side * side)

square(input("Введите одну сторону квадрата: "))
 