
# Методы разбиения и склеивания строк

full_name = 'Sergei Vladimirovich Kochkin'

name_index =full_name.find(' ')
name = full_name[:name_index]
print(name)

surname_index = full_name.rfind(' ')
surname = full_name[surname_index+1:]
print(surname)

patronymic = full_name[name_index + 1:surname_index]
print(patronymic)


# split() - Разбивает строку на части (подстроки) по выбранному разделителю и возвращает список.
full_name_list = full_name.split()
print(full_name_list)

name = full_name_list[0]
patronymic = full_name_list[1]
surname = full_name_list[2]
print(name)
print(patronymic)
print(surname)

langs = 'Python, Java, JavaScript, Ruby, TS, GO, PHP'
langs_list = langs.split(', ') # Разбиение по символу
print(langs_list)

students = 'Sergei,Vadim,Jon,Djon'
students_list = students.split(',')
print(students_list)

students_list_limit = students.split(',',1)
print(students_list_limit)

string_with_tabs = "Vadim\nZviagintsev School" # Табуляция засчитывается как пробел
print(string_with_tabs.split())

ip_address = "192.168.1.1"
parts = ip_address.split(".")
print(parts)  # ['192', '168', '1', '1']

print(type(parts))                  # возврощает тип
print(isinstance(parts, list))      # сравнивает тип данных



# .join() - Соединяет элементы списка (или другого итерируемого) в строку, вставляя между ними разделитель

country = ['Russia','India','Japan','USA']
country_str = ' '.join(country)
print(country_str)

url_parts = ['http:/','russian-it-academy.ru','kursyi']
url = '/'.join(url_parts)
print(url)

file_path_parts = ['C',"home", "user", "documents", "file.txt"]
file_path = '/'.join(file_path_parts)
print(file_path)

n = str(file_path_parts)
print(n)
