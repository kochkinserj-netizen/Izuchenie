import random
import math
# Знакомство с модулем random
# Модуль используется для создания тестовых данных

num = random.random() * 100
print(num)

# random.random() -> [0.0, 1.0)  результат float
rand_int = random.random() * 100
print(rand_int) # В ответ приходит float
print(round(rand_int))
print(math.floor(rand_int))

# random.uniform() ->  [start, end] результат float
rand_num2 = random.uniform(10,20)
print(rand_num2)

# rondom.randint(start, end) -> [start, end]  результат int
# генерация целых чисел
rand_num1 = random.randint(0,10)
print(rand_num1)


# random.randrange() -> [start, end, step) -> int
rand_num3 = random.randrange(0,10, 2)
print(rand_num3)

random_even = random.randrange(1,10, 2)
print(random_even)

# random.choice()
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.choice(num_list))

alpha = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(random.choice(alpha))

print(random.choice('abcdefghijklmnopqr'))

names = ['vadim', 'jon', 'greg']
surnames = ['kochkin', 'petorm', 'lukin']
name = random.choice(names)
surname = random.choice(surnames)
full_name = f'{name} {surname}'
print(full_name)

user_age = random.randint(18,100)
print(user_age)

# генерация случайных значений
id = random.randint(1,1000000)
rand_email = f'user_{id}@mail.ru'
print(rand_email)

random_phone = f'8-{random.randint(900,999)}-{random.randint(900,999)}-{random.randint(10,99)}-{random.randint(10,99)}'
print(random_phone)

price = round(random.uniform(10,100),2)
print(price)

