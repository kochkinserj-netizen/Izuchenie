 # Знакомство с числами
# int
age = 30
print(age)
print(type(age))
print(isinstance(age, int))

negative_number = -151
print(negative_number)
print(type(negative_number))
print(isinstance(negative_number, int))

big_number = 123_456_789_123_444
print(big_number)

# float
temperature = 36.6
print(temperature)
print(type(temperature))
print(isinstance(temperature, float))

negative_temperature = -3.65600
print(negative_temperature)
print(type(negative_temperature))
print(isinstance(negative_temperature, float))

# Работа со степенями (здвиг запятой)
a = 10e3
print(a) #10000.0

PI = 3.14159e2
print(PI) #314.159

small_int = 1e-3
print(small_int)

num_1 = 0.1
num_2 = 0.2
summa = num_1 + num_2
print(summa) # 0.30000000000000004

# bool при использовании с арифметическими операторами превращаются в 1 или 0
true = True
print(true)
print(type(true))
print(isinstance(true, bool))

false = False

bool_sum = true + false
print(bool_sum)

print(10-true)

