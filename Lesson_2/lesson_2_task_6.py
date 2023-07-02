#Дан список
lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

for l in range(0, len(lst)):
    if (lst[l] < 30) and (lst[l] % 3 == 0):
        print(lst[l])
