# Проверка вхождения спомощью оператора in

'''
Базовый синтаксис
подстрока in строка
Пример:

"Вадим" in "Здесь был Вадим Звягинцев"   # True
"Vadim" in "Вадим Звягинцев"             # False
'''

name = 'Sergei'
lower_case_name = name.lower()
full_name = 'Kochkin Sergei Vladimirovich'
print(name in full_name)
print(full_name in lower_case_name)

text ='Python QA automation engineer and developer'
print('QA' in text)
print('QA'.lower() in text.lower())

email = 'Sergei_Kochkin@mail.ru'

is_email_exist = '@' in email
print(is_email_exist)

is_dot_sign_exist = '.' in email
print(is_dot_sign_exist)

# отрицание not in
languages = 'Python, Java , JavaScript, Ruby'
search_lang = 'PHP'
is_php_not_learning = search_lang.lower()  not in languages.lower()
print(is_php_not_learning)