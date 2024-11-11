# Strings interpolation

name = 'Duck Killer'
surname = 'Ducky'
age = 3000

print('Me llamo ' + name +', me dicen' + surname + ' y tengo ' + str(age))
print('Me llamo %s, me dicen %s y tengo %d' %(name, surname, age))
print('Me llamo {}, me dicen {} y tengo {}'.format(name, surname, age))
print(f'Me llamo {name}, me dicen {surname} y tengo {age}')

# Desempaquetado
word = 'duck'
d,u,c,k = word

print(d)
print(u)
print(k)
print(c)

# Division
word_slice = word[1:4]
print(f'F{word_slice}')

word_slice = word[-2]
print(word_slice)

word_slice = word[0:2:4]
print(word_slice)

# Reverse
word_slice = word[::-1]
print(word_slice)

# Other string funcions
print(word.capitalize())
print(word.upper())
print(word.count('u'))
print(word.lower())
print(word.isnumeric())
print(word.upper().isupper())
print(word.startswith('du'))