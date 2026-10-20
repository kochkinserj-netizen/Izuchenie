import math

# модуль math - набор готовых методов вычеслений

PI = math.pi
print(PI)

E = math.e
print(E)

# input_in = int(input('Введите положительное число: '))
# print(input_in ** (1/2))
# print(math.sqrt(input_in)) # math.sqrt() - взятие квадратного корня

# округление применяется к float
number = 8.6
number1 = 3.2
number2 = -5.4
# math.floar -> округление вниз
print(math.floor(number))
print(math.floor(number1))
print(math.floor(number2))

# math.ceil -> округлени вверх
print(math.ceil(number))
print(math.ceil(number1))
print(math.ceil(number2))

# возведение в степень
number = 2
print(2 ** 10)
print(math.pow(2,10))
