import json

# Работа с JSON

# JSON - JavaScript Object Notation
# JSON - формат даных типа ключ:значение

# Типы данных JSON

"""
string
number
boolean
null
array - list
object - dict
"""

# Python dict <-> JSON
# Для работы с JSON мы будем использовать пакет/модуль/библиотека json

user = {
    'id': 1,
    'name': 'Sergo',
    'surname': 'Koch',
    'tolls': ['Pythin', 'Pytest', 'HTTPX']
}

# Работа с JSON сводится к 2-м методам

# Сериализация (кодирование) - преврощение Python-обекта в JSON
# json.dumps(dict) - перевод словоря (обекта) в строку JSON
# '{"id": 1, "name": "Sergo", "surname": "Koch", "tolls": ["Pythin", "Pytest", "HTTPX"]}'

user_json = json.dumps(user)
print(user_json)

print(type(user_json))
print(type(user))
# Десериализация (декодирование) - преврощение JSON в Python-обекта
# json.loads(json) - разбор строки JSON в Python обект
user_dict = json.loads(user_json)
print(user_dict)

print(type(user_dict))

# В основных библиотеках для работы с сетью сериализация и десериализация выполняется под капотом
# При тестировании backend используются библиотеки requests, httpx, json.dumps писать не нужно








