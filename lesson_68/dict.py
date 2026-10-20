# Знакомство со словарем

# Словарь - это колекция пар "ключ:значение", где каждый ключь уникальный

empty_dict = {}
print(empty_dict)
print(type(empty_dict))

user = {
    'id':152,
    'name': 'Sergei',
    'surname':'Kochkin',
    'age':30,
    'is_maried':True,
    'friends':['Mick','Alex','Artem','Vasilii'],
    # 'id': 0, произойдет перезапись первой пары ключ значения!
    'occupation': {
        'title':'Programming',
        'company':'Computer Science',
        'salary':120_000
    }
}

# Ключи должны быть уникальны в противном случае произайдет перезапись значения
# Ключом может любой тип данных (практически всегда строка)
# значением может быть любой тип данных

print(user)

dict_training = {
    'id':152,
    5 : 'five',
    3.14: 'pi',
    False : 'false',
    (1,2,3):'tuple',
    None : 'NoneType Value',
    # [1,2]:'value'  Ключ должен быть неизменяемым типом данных
}
print(dict_training)

# для получения значенияобращаемся по ключу
print(user['id'])
print(user['name'])
print(dict_training[5])
print(dict_training[False])

# способы создания словарей
# через литерал словоря
course = {
    'title':'Programming',
    'company':'Computer Science',
    'duration':5,
    'price': 50_000
}
print(course)

# создание словоря и добавление ключей и значений
# teacher = {}
teacher = {}
print(teacher)

teacher['title'] = 'Teacher'
teacher['company'] = 'Computer Science'
teacher['id'] = 1

# через функцию dict
country = dict(name='Russia', capital='Moscow', population=140_000_000)
print(country)

brand = 'BMW'
model = 'X5'
price = 200_000
year = 2020

car = dict(brand=brand, model=model, price=price, year=year)
print(car)

auto = {
    'brand': brand,
    'model': model,
    'car_price': price,
    'year': year
}
print(auto)


# функция dict + список кортежей

capital = dict([('city','Moscow'),('population', 140_000_000),('mayor','Sobyanin')])
print(capital)
