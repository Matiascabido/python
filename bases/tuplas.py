# Tuplas
verduleria = tuple()
verduleria = ()
verduleria = ('papa', 35, 'batata', 2, 'pera', 90)

print(verduleria)
print(type(verduleria))
print(verduleria[2])
print(verduleria[-1])

# Busqueda de vairables repetidas
print('TOTAL VERDU: ', verduleria.count('papa'))

# Ubicacion de una variable en la tupla
print('UBICACION PERA: ', verduleria.index('pera'))

# Nuevo conjunto con otra tupla
otra_verdu = ('zanahoria', 23, 'pepino', 40)
print('LAS VERDU: ', verduleria + otra_verdu)

# Sub conjunto de una tupla
otra_verdu = ('zanahoria', 23, 'pepino', 40)
print('LAS VERDU 2: ', otra_verdu[0:2])


# Principales diferencias con las LISTAS

'''
=> Las tuplas solo tienen dos funciones
  "index" y "count".

=> Las tuplas no son mutables.

=> La inicializacion de una tupla,
  se puede identificar por los parentesis () / tupla().

'''