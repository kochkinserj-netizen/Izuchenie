import json
# Работа с JSON

# JSON JavaScript Object Notation


'''
Соотношение типов данных в JSON
String      ->  ''              str
Number      -> 1,2 ,2.5         int,float
Boolean     -> true,false       True, False
null        -> null             None
Object      -> {}               dict
Array       -> []               list
'''



'''
JSON по сети передается как строка
"{
    'user':1,
    'first_name':'George',
    'last_name':'Harry',
}"
'''

# Методы пакета JSON
# dumps: сериализация    - преобразование словаря в JSON - сторку
# loads: парсинг         - преобразование JSON - стороки в словарь

user = {
    'user_id':1,
    'first_name':'George',
    'last_name':'Harry',
}

print(user)
print(type(user))

user_str = json.dumps(user)
print(user_str)
print(type(user_str))

teacher = {
    'user_id':1,
    'first_name':'Сергей',
    'last_name':'Кочкин',
}

#  При работе с кирилицей запрос выводится в кодировке
# UTF-8
#
teacher_str = json.dumps(teacher)
print(teacher_str) # {"user": 1, "first_name": "\u0421\u0435\u0440\u0433\u0435\u0439", "last_name": "\u041a\u043e\u0447\u043a\u0438\u043d"}
print(type(teacher_str))

# Для рааботы с кирилицей вызывается метод ensure_ascii=False
# для удобства чтения indent=4
teacher_string = json.dumps(teacher , ensure_ascii=False, indent=4)
print(teacher_string) # {"user": 1, "first_name": "Сергей", "last_name": "Кочкин"}
print(type(teacher_string))

# loads
user_data = '{"user_id":1,"first_name":"George","last_name":"Harry","age": 19}'
print(user_data)
print(type(user_data))

user_dict = json.loads(user_data)
print(user_dict)
print(type(user_dict))
print(user_dict['user_id'])

# На уровне библиотек аввтотестов это происходит  под капотом
# нам практически не прийдется выполнять конвертации руками

# dump - запись JSON в файл
# load - чтение JSON из файла