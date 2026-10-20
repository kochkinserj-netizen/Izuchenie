# Методы set

countries = {'USA', 'Canada', 'Mexico', 'Brazil', 'Italy'}

print(countries)
print(type(countries))

# добавление элементов

countries.add('Peru')
print(countries)

# при повторном добавлении ничего не произойдет

countries.add('USA')
print(countries)

# remove() - небезопасное удаление (используем if)

removable_country = 'USA'
if removable_country in countries:
    countries.remove(removable_country)
    print(f'{removable_country} deleted')
else:
    print(f'{removable_country} not in countries')
print(countries)

# discard() - безопасное удаление (работает даже если элемента во множестве нет)

countries.discard('Peru')
print(countries)
countries.discard(removable_country)
print(countries)

# pop() - случайное удаление

# clear() - полная очистка множества

tools = {'Python', 'Java', 'PHP', 'JavaScript'}
tools_ref = tools

print(tools_ref is tools)

tools.add('Allure TestOps')
print(tools)
print(tools_ref)

# copy() - создание копии set

tools_copy = tools.copy()

print(tools_copy is tools)
tools_copy.add('Github')
print(tools_copy)
print(tools)

backend_tools = {'FastAPI', 'SQLAlchemy', 'Pydantic', 'RabbitMQ', 'Celery'}

# for tool in backend_tools:
#     tools.add(tool)
# print(tools)

tools.update(backend_tools)
print(tools)

# update() - добавление элементов итерируемых элементов во множество

frontend_tools = ['TypeScript', 'React', 'Zustand']
monitoring_tools = ('Grafana', 'Jupyter', 'Kibana')

tools.update(frontend_tools,monitoring_tools,backend_tools) # добавляет все коллекции во множество
print(tools)