# Основные операции со множествами

langs = {'Java', 'Pythin', 'JavaScript', 'Go', 'PHP', 'TypeScript', 'Ruby', 'Java'}

print(len(langs))

langs.add('Java')
langs.add('Swift')
langs.add('Kotlin')

print(langs)
print(type(langs))
print(len(langs))

for l in langs:
    print(l)


csherp = 'C#'

if csherp not in langs:
    langs.add(csherp)
else:
    print(f'{csherp} already in the set')

print(langs)

print('Go' in langs)
print('Pascal' in langs)

# Методы set

# add(value) - добавление во множество
langs.add('C++')
print(langs)

# remove(value) - небезопасное удалени по значению

langs.remove('Go')
print(langs)
# если значения нет то будет KeyError
# langs.remove('Fortran') # KeyError: 'Fortran'
print(langs)

if 'Fedora' in langs:
    langs.remove('Fedora')
else:
    print(f'Fedora not in the set')


# discard(value) - безопасное удаление по значению
# если значения во множестве нет то ничего не произойдет

cobol = 'Cobol'
langs.discard(cobol)
print(langs)

# pop() - удаляет произвольный элемент из множества
langs.pop()
print(langs)

# clear() - очистка множества
langs.clear()
print(langs)






