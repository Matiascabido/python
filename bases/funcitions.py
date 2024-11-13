# Functions

def vacaciones (ubicacion):
    print('Estoy en: ', ubicacion)
    if ubicacion == 'brasil':
        vacaciones('que lugar feo')

vacaciones('miramar')
vacaciones('la paloma')
vacaciones('brasil')

def calcularDistancia(x: int, y: int):
    return int(y) - int(x) 

print('Distancia entre 20 y 44:', calcularDistancia(20, 44))
print('Distancia entre 200 y 44:', calcularDistancia('200', 44))

# Recursividad
def calcularDistancia(x: int, y: int):
    if x != 20:
        calcularDistancia(20, y)
    return int(y) - int(x) 

print('Distancia entre 20 y 45:', calcularDistancia(20, 45))
print('Distancia entre 21 y 44:', calcularDistancia(21, 44))

# Default
def vacaciones (ubicacion = 'Brasil'):
    print('Estoy en: ', ubicacion)
    
vacaciones()

# Multiples Variables
def vacaciones (*ubicaciones):
    for ubi in ubicaciones:
        print('Estoy en: ', ubi)
    
vacaciones('Miami', 'Japon', 'Atun')
vacaciones('Japon', 'Corea')

def vacaciones (*ubicaciones):
    print('Estoy en: ', ubicaciones)
    
vacaciones('Miami', 'Japon', 'Atun')
vacaciones('Japon', 'Corea')
