# Исследование цикла for

# В циклах используют переменные i, j ,k ,l ,m ,n - пременная, хронящая значение для каждой итерации
# Первый способ создания через range
for i in range(10):
    print(i)


cities = ['Moscow', 'Kazan', 'Krasnodar', 'Omsk', 'Sochi']

# Второй способ создания цикла for - обход колекции
for city in cities:
    print(city.lower())

full_name = 'Sergei Kochkin'

for latter in full_name:
    print(latter)

domains = {'ru', 'com', 'uk', 'info'}
for domain in domains:
    print(domain)

courses = ('java', 'python', 'javascript', 'c#')
print(courses)

courses_list = list(courses)
for i in range(len(courses_list)):
    print(f'На {i} позиции/индексе хранится следущее значение {courses_list[i].capitalize()}')

# после цикла переменная i стирается из памяти, т.к. она видна в блоке кода после цикла

# Управление циклом:break - выход из цикла,прирыв цикла
for i in range(10):
    if i == 6:
        break
    print(i)
print('After loop')

# continue - пропуск значения удовлетворяющее условию

for i in range(40):
    if not i % 2:
        continue
    print(i)

string = 'Python qa automation'
count = 0
for later in string:
    if later == 'a':
        count += 1
print(count)