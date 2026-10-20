# Распаковка списков

technologies = ['Python','Pytest','Allure']

lang = technologies[0]
automation_tools = technologies[1]
reporting = technologies[2]

print(lang)
print(automation_tools)
print(reporting)

# Распоаковка списка
Python, auto_tool, report_tool = technologies # Колличество переменных должно совпадать с длинной списка
print(Python)
print(auto_tool)
print(report_tool)

address = ['Russia', 'Moscow region', 'Moscow', 'Kosmonavtov St', 15 , 220]
print(len(address))

country, region, city, *postal_addr = address # '*' - rest оператор присваивает список оставшихся значений в список
print(country)
print(region)
print(city)
print(postal_addr)

full_name = ['Jack','Jerry', 'Larry', 'Barron','Mitchel' , 'Billy', 'Clark']
first_name, *middle_name, last_name = full_name
print(first_name)
print(middle_name)
print(last_name)
# *rest переменной прискаивается список


def show_full_name(f_name, m_name, l_name):
    print(f'{f_name} {m_name} {l_name}')


show_full_name('Sergei', 'Vladimirovich', 'Kochkin')


def show_fio(*args):
    print(args)
    print(type(args))
    name, patronymic, surname = args
    print(name)
    print(patronymic)
    print(surname)


show_fio('Sergei', 'Vladimirovich', 'Kochkin')

# Передача списка как аргументы
numbers = [5, 10, 15]


def multiply(a, b, c):
    print(a * b * c)


multiply(*numbers)

