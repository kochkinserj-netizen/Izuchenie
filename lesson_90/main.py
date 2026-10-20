# Встроенные функции для работы с коллекциями и итерациями
from functools import reduce
# map — применение функции к каждому элементу

salaries = [100_000,200_000,300_000]

employees = [
    {
        'id':1,
        'name':'sergei',
        'salary':400_000,
            },{
        'id':2,
        'name':'jim',
        'salary':300_000,
            },{
        'id':3,
        'name':'Henry',
        'salary':250_000,
    }
]
# list comprehension
upgraded_salaries = [s * 1.2 for s in salaries]
print(upgraded_salaries)

# Функция map(func, iterable, ...) применяет переданную функцию func к каждому элементу итерируемого объекта

def upgrad_salary(salary:int) -> float| int:
    return salary * 1.2
# map через ранее объявленную функцию
increased_salaries = list(map(upgrad_salary, salaries)) # Что бы получить map нужно использовать list
print(increased_salaries)
# map через lambda
indexed_salaries = list(map(lambda s : s * 1.2 , salaries))
print(indexed_salaries)

# map для списка словарей

employees_with_indexed_salaries = list(map(lambda employee: {
    **employee,
    'salary':int(employee.get('salary',0) * 1.1)
}, employees))


print(employees_with_indexed_salaries)


# filter — отбор элементов по условию

# list comprehension
high_salaries = [s for s in salaries if s > 250_000]
print(high_salaries)

# filter(predicate, iterable) возвращает итератор,
# содержащий только те элементы,
# для которых predicate возвращает истинное значение.


def salary_filter(salary:int) -> bool:
    return salary > 250_000

hude_salary = filter(salary_filter, salaries)
print(list(hude_salary))

six_digit_salaries = list(filter(lambda s: s >= 100_000, salaries))
print(six_digit_salaries)

# filter для списка словарей

senior_employees = list(filter(lambda employee: employee.get('salary',0)>300_000, employees))
print(senior_employees)

# reduce — свёртка коллекции в одно значение

# Функция reduce применяет переданную функцию к парам элементов последовательно,
# «сворачивая» итерируемый объект в единственное накопленное значение.
# Это классический паттерн fold (свёртка) из функционального программирования.

# reduce(function, iterable[, initializer])

salaries_sum = reduce(lambda accumulator,current_salary: accumulator + current_salary, salaries, 0 )
print(type(salaries_sum))# значение полученное из функции reduce
print(salaries_sum)

# reduce  для списка словарей

employees_salary = reduce(lambda accumulator,current_employee: accumulator + current_employee.get('salary',0), employees, 0 )
print(employees_salary)

# Функции-агрегаторы: max, min, sum
# Для примитивов все просто
min_salary = min(salaries)
print(min_salary)

max_salary = max(salaries)
print(max_salary)

sum_salary = sum(salaries)
print(sum_salary)

# max(iterable, *, key=None)
# min(iterable, *, key=None)
# sum(iterable, start=0)

max_employee = max(employees, key=lambda employee: employee.get('salary',0))
print(max_employee)

min_employee = min(employees, key=lambda employee: employee.get('salary',0))
print(min_employee)

# Проверочные функции: all и any
# all(iterable) — возвращает True, если все элементы истинны (или iterable пуст).
print(all(s > 0 for s in salaries))


# any(iterable) — возвращает True, если хотя бы один элемент истинен (для пустого — False).

print(any(s > 110_000 for s in salaries))
