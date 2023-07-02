#Напишите функцию fizz_buzz, которая принимает один аргумент — n (число).
#Функция должна печатать числа от 1 до n. При этом:
#   1. если число делится на 3, печатать `Fizz`;
#   2. если число делится на 5, печатать `Buzz`;
#   3. если число делится на 3 и на 5, печатать `FizzBuzz`
def fizz_buzz(n):
    for n in range(1, n):
        if (n % 3 == 0) and (n % 5 == 0):
            print('FizzBuzz')
        elif (n % 5 == 0):
            print('Buzz')
        elif (n % 3 == 0):
            print("Fizz")
        else:
            print(n)
fizz_buzz(n = int(input("Введите целое число: ")))