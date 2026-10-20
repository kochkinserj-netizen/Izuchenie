import math
# знакомство с функцией округления round()

num1 = 13.2
num2 = 4.7
print(math.floor(num1))
print(math.ceil(num1))

print(round(num1))
print(round(num2))

PI = math.pi
print(PI)

print(round(PI, 2))
print(round(PI, 3))
print(round(PI, 4))

# round(число, количество символов после запятой)
print(round(PI, 5))

# Python округляет к ближайшему чётному числу, если дробная часть ровно .5.
print(round(5.5))
print(round(6.5))

