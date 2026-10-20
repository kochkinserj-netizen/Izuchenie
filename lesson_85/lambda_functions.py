# Лямбда-функции
from lesson_79.variables_scope import square


def get_full_name(first_name: str, last_name: str) -> str:
    return f'{first_name.title()} {last_name.title()}'

get_fio = lambda name,surname: f'{name} {surname}'

print(get_fio('Sergei','Kochkin'))

#square

square = lambda n: n**2
print(square(5))

is_even = lambda n: n % 2 == 0
print(is_even(5))

# map c лямбдой
# трансформация каждого элемента списка
names = ['анна', 'иван', 'мария']

def transform_names(name: str) -> str:
    return name.title()

# upper_names = list(map(transform_names, names))
upper_names = list(map(lambda name: name.upper(), names))

print(upper_names)

# filter с лямбдой

# проверка что каждый элемент соответствует исловиям

numbers = [1, -2, 3, -4, 5, 0, -7, 9]

def get_positiv_numbers(number):
    return number > 0

# positiv_numbers = list(filter(get_positiv_numbers, numbers))
positiv_numbers = list(filter(lambda number:number > 0, numbers))
print(positiv_numbers)

# фильтрацию предпочтительно делать через list comprehension
pos_numbers =[n for n in numbers if n > 0]
print(pos_numbers)

# sorted с лямбдой
# Лямбда часто используется как ключ сортировки.

students = [
    {"name": "Иван", "score": 85},
    {"name": "Анна", "score": 92},
    {"name": "Пётр", "score": 78}
]

# Сортируем по полю 'score'
best = sorted(students, key=lambda s: s["score"], reverse=True)
print(best)  # Анна, Иван, Пётр


def sort_by_score(student):
    return student.get("score", 0)


sorted_students = sorted(students, key=sort_by_score, reverse=True)
print(sorted_students)

# Комбинация map и filter
# квадраты положительных чисел
squares = list(map(lambda x: x**2, filter(lambda x: x > 0, numbers)))
# list comprehension
squares1 = [x**2 for x in numbers if x > 0]
print(squares)
print(squares1)

students = [
    {"id":1,"name": "Иван", "score": 85},
    {"id":2,"name": "Анна", "score": 92},
    {"id":3,"name": "Пётр", "score": 78}
]

ids = list(map(lambda s: s.get("id", None), students))
print(ids)
