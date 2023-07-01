# Создайте функцию is_year_leap, принимающую 1 аргумент — год (число) — и возвращающую True, если год високосный, и False — иначе.
is_year_leap = input("Введите год: ")
    
if (int(is_year_leap) % 4 == 0):
    print("год ", is_year_leap, ":", True)
else:
    print("год ", is_year_leap, ":", False)