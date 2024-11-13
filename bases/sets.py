# Sets 
hollywood = set()
hollywood_set = {}

print(hollywood)
print(type(hollywood)) 
print(type(hollywood_set)) # type 'diccionario'

hollywood_set = { 'Pixar', 'Warner Bro', 69, 'Marvel'}
print(type(hollywood_set)) # type 'set'

# Tamaño del set
print('Tamaño del Set_origen: ', len(hollywood))
print('Tamaño del Set_alt: ', len(hollywood_set))

# Estructura desordenada
hollywood_set.add(45)
print(hollywood_set)

# No admite repetidos
hollywood_set.add('Pixar')
print(hollywood_set)

# Eliminar repetidos de un set
hollywood_set_2 = { 'a', 'b', 'c', 'a'}
hollywood_set_2 = set(hollywood_set_2)
print('Elimina repetido {"a", "b", "c", "a"} =>', hollywood_set_2)

# Remover un elemento de un set
hollywood_set_2 = { 'a', 'b', 'c'}
hollywood_set_2.remove('b')
print('Se elimina "b" en {"a", "b", "c"} =>', hollywood_set_2)

# Buscar un elemento en un set
hollywood_set_2 = { 'a', 'b', 'c'}
print('Existe "c" en {"a", "b", "c"} =>', "c" in hollywood_set_2)

# Limpiar set
hollywood_set_2.clear()
print('Tamaño del Set_alt_2: ', len(hollywood_set_2))

# Unir dos sets
hollywood_set_2 = {'Pixar', 'Warner Bro', 'DreamWorks', 'Lucas Films'}
hollywood = hollywood_set.union(hollywood_set_2)
print('El total de sets: ', hollywood)

# Diferencias
print('Diferencias entre sets: ', hollywood_set_2.difference(hollywood_set) )
