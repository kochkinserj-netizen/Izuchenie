# Функции int() и float() для преобразования типов

# name = input('Please enter your name: ')
# print(name)
# print(type(name))

#функция int() принимает аргумент и преобразует его в число
# результат функции число либо ошибка значения
# age = input('What is your age?')
# print(age)
# print(type(age))
# age = int(age)
# print(age)
# print(type(age))

print(int('10'))
print(type(int('10')))

#при работе с float дробная состовляющая отбрасывается
print(int(3.45))
print(int(3.89))

# print(int('sergo')) # ValueError: invalid literal for int() with base 10: 'sergo'
# print(int('3.89'))
#
# price = input('Enter price: ')
# price = float(price)
# print(price)

print(float(3.89))
print(float('3.89'))
# print(float('3,89'))


num1 = 10
num2 = '5'
summa = num1 + float(num2)
print(summa)
