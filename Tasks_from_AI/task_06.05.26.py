# задачки от ИИ
import math
import random

# 1.
# name = input('Введите свое имя: ')
# print(f'Привет {name}')

# 2. Регистр имени

# name = input('Введите свое имя: ').lower()
# print(name.title())

# 3. Цензура

# string = 'Python is awesome and fun'
# new_string = string.replace('awesome', 'cool')
# print(new_string)

# 4. Удаление лишнего

# phone = '  + 7 (912) 736 10 94'
# phone_formating = (phone.replace(' ', '')
#                    .replace('(','')
#                    .replace(')','')).strip()
# print(phone_formating)
#
# phone_formatig2 = ''
# for p in phone:
#     if p == '(':
#         continue
#     elif p == ')':
#         continue
#     elif p == ' ':
#         continue
#     phone_formatig2 += p
#
# print(str(phone_formatig2)

# 5. Анализ почты

# email = input("Enter your email: ")
# print('@' in email)
# print(email.startswith('@'))
# print(email.endswith('.ru'))
# print(email.endswith('.com'))

# 6.

# input_full_name = input("Please enter your full name: ")
#
# if ' ' in input_full_name:
#     name = input_full_name[:input_full_name.index(' ')]
#     surname = input_full_name[input_full_name.index(' ') + 1:]
#     print(name[::-1])
#     print(surname[::-1])
# else:
#     print('Вы ввели без пробела')


# 7. Площадь круга

# input_rad = float(input('Введите радиус чтобы получить площадь круга: '))
# PI = math.pi
# s = input_rad ** 2 * PI
# print(f'Площадь круга равна: {s}')

# 8. Random_phone

phone = (f'8-9{random.randint(0,9)}{random.randint(0,9)}'
      f'-{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}'
      f'-{random.randint(0,9)}{random.randint(0,9)}'
      f'-{random.randint(0,9)}{random.randint(0,9)}')
print(type(phone))
print(phone)