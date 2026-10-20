# Практика при работе с типами данных

# Создать переменные и присвоить и значения: название страны,сталица, население страны, список крупных городов, является сталлица самым населенным городом

country = 'Russia'
capital = 'Moscow'
population_country = 238_585_000
list_big_cities = ['Moscow', 'Piter', 'Sochi']
is_capital_most_populated_city = True  # Логические переменные называем начиная на is

# Для каждой переменной вывести тип данных
print(type(country))
print(type(capital))
print(type(population_country))
print(type(list_big_cities))
print(type(is_capital_most_populated_city))

# Для каждой переменной сверить пренадлежит ли она тому или иному типу данных
print(isinstance(country, str))
print(isinstance(capital, str))
print(isinstance(population_country, int))
print(isinstance(list_big_cities, list))
print(isinstance(is_capital_most_populated_city, bool))

# список европейскх стран
europe_country = ['Russia', 'Belarus','Italy','France']
print(europe_country)
print(type(europe_country))
print(isinstance(europe_country, list))

# кортеж языков програмирования
languages_programming = ('Python', 'PHP', 'Java', 'C++')
print(languages_programming)
print(type(languages_programming))
print(isinstance(languages_programming, tuple))

# множество столиц
capitals = {'Moscow', 'Rome', 'Minsk', 'New York', 'Kiev'}
print(capitals)
print(type(capitals))
print(isinstance(capitals, set))

# создать словарь описывающий нас
# Ключи словоря: name: str, surname: str, age: int, salary: float, tools: [str], is_married: boolean

it_me = {
    'name' : 'Sergei',
    'surname' : 'Kochkin',
    'age' : 30,
    'salary' : 310_000.50,
    'tools' : ['DevTools', 'Swagger', 'Postman', 'DBeaver', 'PyCharm'],
    'is_married' : True,
}
print(it_me)
print(type(it_me))
print(isinstance(it_me, dict))

