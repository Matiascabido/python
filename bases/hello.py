print('Hello Mati')

# Comentario lineal
"""
Comentario multiples
Lineas
"""
'''
  Comentario multilena
  con coma simple
'''

# Tipos de datos
print(type('Soy un String'))    # String
print(type(3))                  # Int
print(type(2.3))                # Float
print(type(1+4j))               # Complex
print(type(3//4))               # Int
print(type(True))               # Bool


# Concatenacion
print('Hello', ',', 'World', '!')
print('Hello', ',', str(12), True)
print(
    len(str(12)), 
    len([str(12), True]),
    len({str(12), True}),
    len(''), 
    len([]), 
    len({}),
)

# Repete
print('Hola, ' * 4)