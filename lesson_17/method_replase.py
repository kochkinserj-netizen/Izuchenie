# знакомство с методом replase() -
# метод replase() - делает замену старой подстроки на новую N раз
# string.replase(old,new,count)

text = ('Hello World')
new_text = text.replace('World','Python')
print(text)
print(new_text)

string = ' Сергей Kochkin in a student Сергей Kochkin'
new_string = string.replace('Сергей','Sergei')
print(new_string)

new_string_v1 = string.replace('Сергей','Sergei',1)
print(new_string_v1)

# замена символов внутри текста/удаление
phone_number = '8-912-737-10-98'
print(phone_number.replace('-',''))

full_name = 'Sergei_Vladimirovich_Kochkin'
print(full_name.replace('_',' '))

# происходит замена всех совпадений
text = "cat catalog scatter"
new_text = text.replace('cat','dog') # неправельно
print(new_text)

new_text = text.replace('cat','dog',1)
print(new_text)


# каскадное изменение символов
phone_number = '8-912 737 10-98'
phone = phone_number.replace('-','').replace(' ','')
print(phone)

phone_number = '8(912)737-10-98'
phone = (phone_number.replace('-','')
         .replace('(','')
         .replace(')',''))
print(phone)

#если совпадений не найдено то строка возврощается в том же виде
