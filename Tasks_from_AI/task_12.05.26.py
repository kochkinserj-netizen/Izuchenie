# user_input = float(input('Enter a number: '))
#
# if user_input > 1e1000:
#     print('int')
#


# Задача на фазу дня

# user_input_hour = int(input("Enter hour: "))
# if 0 <= user_input_hour <= 5:
#     print('Ночь')
# elif 6 <= user_input_hour <= 11:
#     print('Утро')
# elif 12 <= user_input_hour <= 17:
#     print('День')
# elif 18 <= user_input_hour <= 23:
#     print('Вечер')
# else:
#     print('По мойму ты что то перепутал')

# сумма четных чисел до 50

summa = 0

for i in range(50):
    if i % 2 == 0:
        summa += i
print(summa)

# Таблица умножения до 5

x = 1
for i in range(10):
    if i > 9:
        x += 1
    print(f'{x}*{i}={x*i}')

