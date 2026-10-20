# методы обрезки строки
# strip,lstrip,rstrip

full_name = 'Sergei Kochkin                '
print(full_name)

cleaned_full_name = full_name.strip()
print(cleaned_full_name)

text = '\tSergei\n Kochkin\n'
print(text)
clean_text = text.strip()   # обрезка только по краям
print(clean_text)

# Удаление конкретных символов

text = '-----School of Information Technology---'
clean_text = text.strip('-')
print(clean_text)

string = '#@-Sergo@++'
print(string)
clean_string = string.strip('#@-+')
print(clean_string)

random_sym = '/*/*//***///**/Sergei Kochkin///*/*/*/*/*/**/'
clean_random_sym = random_sym.strip('*/ ')
print(clean_random_sym)

# lstrip, rstrip - удаляют символы слева и спроава соответственно. Правила такие же как и для strip

full_name = '         Sergei Kochkin       '
print(full_name.lstrip())
print(full_name.rstrip())

text = '!@#$%^&*()Sergo!@#$%^&*()'
print(text.lstrip('!@#$%^&*()'))
print(text.rstrip('!@#$%^&*()'))

name = 'Sergei Kochkin'
print(name.strip('s')) # регистр имеет значение (удаление не будет)



