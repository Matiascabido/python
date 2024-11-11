# Invalid variable names
'''
    first-name
    first@name
    first$name
    num-1
    1num
'''

# /////////////////////////////////// #

# Variables [* best practices *]

text = 'Do cillum enim labore esse exercitation irure fugiat et.'
print(text)

super_text = 'Eiusmod voluptate eiusmod sunt elit minim aliquip tempor do aliquip deserunt.'
print(super_text)

super_duper_text = 'Duis officia id fugiat amet consectetur esse commodo sunt cillum.'
print(super_duper_text)


# /////////////////////////////////// #

# Variables [* others types declaration *]

super_int_variable = 10
print(super_int_variable)

super_bool_variable = True
print(super_bool_variable)

super_text_variable = '22'
print(super_text_variable)

# /////////////////////////////////// #

# Variables [* data transformation *]

from_int_to_str = str(super_int_variable)
print(
    type(super_int_variable),
    super_int_variable,
    type(from_int_to_str),
    from_int_to_str
)

from_str_to_int = int(super_text_variable)
print(
    type(super_text_variable),
    super_text_variable,
    type(from_str_to_int),
    from_str_to_int
)

# /////////////////////////////////// #

# Variables [* declaracion en una sola linea *]

name, last_name, alias, hours, active = 'Duck', 'Killer', 'Duck', 3000, False

print('Player:', name, last_name, 'Alias:', alias,'Hours:', hours, 'Active:', active)

# /////////////////////////////////// #

# Variables [* inputs *]

# firts_name = input('Como te yamas? ')
# alias = input('Alias tene? ') # Se reasigna un valor previamente asignado.
# age = input('Cuantos años tene?')

# print('Name', firts_name, 'Age', age, 'Alias', alias)

# /////////////////////////////////// #

# Variables [* tipado *]

paragraph: str = 'Ipsum proident velit dolor ad irure enim eu in eiusmod ut ex aute.'
print('Paragraph', paragraph, type(paragraph))
paragraph = len(paragraph)
print('Paragraph', paragraph, type(paragraph))

# /////////////////////////////////// #