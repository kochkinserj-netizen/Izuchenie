
full_name = 'sergei kochkin'
print(full_name)

# .upper() - перевод строки в верхний регистр
upper_full_name = full_name.upper()
print(upper_full_name)
print(full_name)

# .lower() - перевод строки в нижний регистр
user_email = 'SergeiKochkin@Gmaill.su'
lower_case_email = user_email.lower()
print(lower_case_email)

# .title - каждое слово строки начинается с большой буквы
titled_full_name = full_name.title()
print(titled_full_name)
# если исходная строка в верхнем регистре то .title() оставит заглавными телько первые буквы слов
title_upper_full_name = full_name.title()
print(title_upper_full_name)

# .capitalize() - первая буква строки с большой строки
sentence = 'мы изучаем язык програмирования python'
capitalized_sentence = sentence.capitalize()
print(capitalized_sentence)

capitalized_upper_full_name = upper_full_name.capitalize()
print(capitalized_upper_full_name)

# .swapcase()
school = 'Sergei Kochkin in jobs Thesis'
swapcase_scholls = school.swapcase()
print(swapcase_scholls)

# .islower(); .isupper(); .istitle() - возврощает булево значение при проверке соответствующего метода
islower_full_name = full_name.islower()
print(islower_full_name)
isupper_full_name = full_name.isupper()
print(isupper_full_name)
istitle_full_name = full_name.istitle()
print(istitle_full_name)

name = 'sergei'
surname = 'KOCHKIN'
full_name = name +" "+ surname
print(full_name)
full_name = full_name.title()
print(full_name)
print(full_name.islower())
print(full_name.isupper())
print(full_name.istitle())
swapcase_full_name = full_name.swapcase()
print(swapcase_full_name)