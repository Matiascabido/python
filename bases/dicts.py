# Diccionarios
ingles = dict()
spanish = {}

# Tipo diccionario
print(type(ingles))
print(type(spanish))

ingles = dict({
    "casa": "home",
    "nombre": "name",
    "apellido": "lastName",
    "edad": "age",
    "Tia": {'Mabel', 'Hermenegilda', 'Sonia'}
})
spanish = {
    "casa": "home",
    "nombre": "name",
    "apellido": "lastName",
    "edad": "age",
    2: 'Mabel'
}

# Tipo diccionario
print(type(ingles))
print(type(spanish))


print('Dict en: ', ingles)
print('Dict es: ', spanish)

# Tamaño del diccionario
print('Tamaño dict en: ', len(ingles))
print('Tamaño dict es: ', len(spanish))

# Invocar un elemento
print('Ostia tia ', ingles['Tia'])

# Reasignar valor a un campo
spanish['casa'] = 'moje'
print('Nueva Casa: ', spanish)

# Agregar un campo nuevo
spanish['monje'] = 'Shaolin'
print('Nueva Casa: ', spanish)

# Eliminar un campo
del spanish[2]
print('Volamos a Mabel: ', spanish)

# Ubicar un valor
print('Existen las tias: ', 2 in spanish)


# Limpiamos el dic
ingles.clear()
print('Dict en: ', ingles)

# Retornar todas las keys
print('Dict key es: ', spanish.keys())

# Retornar todos los valores
print('Dict val es: ', spanish.values())

# Crear diccionarios con keys pero sin datos
new_dict = dict.fromkeys(('Tias', 'Tios'))
print('Nuevo dic: ', new_dict)

new_dict = ['A', 'B', 'C']
print('Nuevo dic: ', dict.fromkeys((new_dict))) 