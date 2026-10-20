# Tuple  в циклах и фунциях


companies = ('kaspersky', 'yandex', 'positive tech', 'lamoda tach', 'x5 tech', 'magnit tech')

# пербор элементов кортежа в цикле for

for company in companies:
    print(company)

# перебор элементов tuple в цикле for с использованием enumerate()

for index, value in enumerate(companies):
    print(f'On {index} index value is {value}')

# вызов функции с переменным числом параметров


def count_sum(*args):
    print(args)
    sum = 0
    for n in args:
        sum += n
    print(sum)

count_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)


# передача в фунцию


def show_info(data):
    print(data)


fio = ('Sergei', 'Vladimirovich', 'Kochkin')
show_info(fio)



def get_user_info():
    name = 'Sergei'
    surname = 'Kochkin'
    age = 30
    return name, surname, age


print(get_user_info())

name, surname, age = get_user_info()
print(name)


def calc_three_numbers(a, b, c):
    return a + b + c


print(calc_three_numbers(5, 7, 9))
numbers = (1, 3, 16,)

print(calc_three_numbers(*numbers)) # * оператор распаковки
print(*numbers)