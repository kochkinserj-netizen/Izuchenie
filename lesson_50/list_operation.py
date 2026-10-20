# Операции со списками

frontend_technologies = ['html', 'css', 'javascript','react','zustand', 'axios']
backend_technologies = ['nestjs', 'prisma', 'rabbitmq','pino']

frontend_automation_technologies = ['python', 'pytest', 'requests', 'httpx', 'pydantic']
backend_automation_technologies = ['pytest', 'requests', 'httpx', 'pydantic']

# конкатенация списков
web_technologies = frontend_technologies + backend_technologies
print(web_technologies)

automation_technologies = frontend_automation_technologies + backend_automation_technologies
print(automation_technologies)

dev_tools = web_technologies + automation_technologies
print(dev_tools)

# Повторение списка n-раз
grades = ['a','b','c','d','e','f']
print(grades * 5)
print(grades*0) # При умнажении на ноль будет пустой список

# Проверка наличия элемента (in,not in) -> True/False

tool = 'redux'
if tool in frontend_technologies:
    frontend_technologies.remove(tool)
    print(f'{tool} is deleted')
else:
    print(f'tool {tool} not in frontend technologies')

new_tech = 'tans query'
if new_tech not in frontend_technologies:
    frontend_technologies.append(new_tech)
    print(f'{new_tech} is added to list')
else:
    print(f'{new_tech} already used')