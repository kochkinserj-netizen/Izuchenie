# Знакомство с set

# Множество — это коллекция уникальных элементов, неупорядоченная и неиндексируемая.

countries = {'England', 'Wales', 'Scotland', 'Northern Ireland'}

print(countries)
print(type(countries))

cities = set() # для создания пустого множества ипользуем функцию set()
print(cities)
print(type(cities))

countries.add("New York") # добавление
print(countries)

print(len(countries))
# print(countries[2]) -> неиндесируемая колекция, нельзя обратится по индексу

countries.add('New York') # при добавлении элементов которые уже есть в set() ничего не происходит
print(len(countries))

students = ['Nick', 'Bill', 'John', 'Nicholas', 'Tom', 'Bill']
students_set = set(students)  # Убераются дубликаты
print(students_set)

# по set можно пройти циклом
for c in countries:
    print(c)

