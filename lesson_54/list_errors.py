# Ошибки при работе с листами

# 1. Индекс вне диапазона

tools = ['Python','Java','C++','Pytest', 'Github']
print(len(tools))

# print(tools[5]) - неправильно

# Рекомендация для проверки
index = 2
if index < len(tools): # Простая проверка по длинне списка
    print(tools[index])

# 2. Ошибка распаковки

python, java, c, pytest, github = tools
# колличество переменных должно равнятся длинне списка

lang, framework, *others = tools
print(lang)
print(framework)
print(others)

# *rest - сохраняется список оставшихся переменных

language,* rest, ci_tool = tools
print(language)
print(ci_tool)
print(rest)

# 3. Ошибки сметодами списков

numbers = [1, 2, 3, 4, 5,]
numbers.append(6)       # ✅ правильно
# numbers.remove(10)      # ❌ ошибка, элемента нет
# numbers.pop(10)         # ❌ индекс вне диапазона
print(numbers)
numbers.insert(0,0)
print(numbers)
num = 10

# При удалении нужно проверить есть ли то что хотим удалить
if num in numbers:
    numbers.remove(num)
else:
    print('num not found')

nums_index = 15
if nums_index < len(numbers):
    numbers.pop(nums_index)
else:
    print('nums_index not found')

# 4. Изменение списка во время перебора

numbers = [1, 2, 3, 4]      # ❌
for n in numbers:           # ❌
    if n % 2 == 0:          # ❌
        numbers.remove(n)   # ❌

print(numbers)
# первый вариант решения- создать новый список
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
old_numbers = []
for n in numbers:
    if n % 2 != 0:
        old_numbers.append(n)
print(old_numbers)

# List comprehension
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

# 5. Ошибка при объединении list и tuple

frontend_technology = ['Python', 'Java', 'C++', 'Pytest', 'Github']
backend_technology = ('Java', 'C++', 'Pytest', 'Github')
full_stack = frontend_technology+list(backend_technology)
print(full_stack)

