# Задачки от искусственного интелекта

# Простое: Создайте переменные разных типов: int, float, str, bool, None.
# Используя type() и isinstance(), проверьте их типы.

num_1 = 1
num_2 = 3.15
string = 'Kudyaplik'
is_married = True
assistant = None

print(isinstance(num_1, type(num_1)))
print(isinstance(num_2, type(num_2)))
print(isinstance(string, type(string)))
print(isinstance(is_married, type(is_married)))
print(isinstance(assistant, type(assistant)))

print('-' * 55) #-------------------------------------------------------------------------------------------------------

# Средняя: Пользователь вводит строку с пробелами. Определите, является ли введенное значение целым числом (int), дробным (float) или строкой (str).
# Подсказка: попробуйте преобразовать типы через int() / float() в try-except, но пока можно использовать .isdigit() и проверку на наличие одной точки.

variable_1 = input('Введи переменную: ')
new_var = variable_1.replace(' ', '').replace('.', '')
print(new_var.isdigit())
print(new_var.isalpha())
print('.' in variable_1 )