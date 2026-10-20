# .isinstance()

name = "Vadim"
# type() - метод возвращает к какому классу принадлежит переменная
# <class 'str'>
print(type(name))

# isinstance(variable, data_type) - это метод возвращающий True или False
print(isinstance(name, str))
print(isinstance(name, int))

print(isinstance(23, int))
print(isinstance(-0, float))

# int
age = 23
print(isinstance(age, int))

# float
temperature = 23.3
print(isinstance(temperature, int))
print(isinstance(temperature, float))

# str
surname = "Kochkin"
print(isinstance(surname, str))

empty_string = ''
print(isinstance(empty_string, str))

# boolean
boolean_value = True
print(isinstance(boolean_value, bool))

# list
students = ['Vadim', 'Sergei']
print(isinstance(students, list))

empty_list = []
print(isinstance(empty_list, list))

# tuple
tools = ('python', 'Java', 'PHP', 'Pytest')
print(isinstance(tools, tuple))

# dict
course = {
    'title':'Python',
    'duration': 2.5,
    'price': 30_000,
}

print(isinstance(course, dict))

# set
cites = {'Moscow', 'Vologda', 'Omsk'}
print(isinstance(cites, set))
# по умолчанию фигурные скобки это словарь а не множество
empty_set = {}
print(isinstance(empty_set, set))

# NoneType
company = None
print(type(company))
print(isinstance(company, type(None)))
# NoneType нужно сравнивать через оператор is
print(company is None)

# type -> class int
# isinstance -> True/False
