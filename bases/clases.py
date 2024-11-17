# Clases

class EmptyPokeball:
    pass # evitar error de ejecucion

print(EmptyPokeball)
print(EmptyPokeball())

# Clase que necesita valores en el constructor
class Pokeball:
    def __init__(self, size, type, name, is_active) -> None:
        self.size = size
        self.type = type
        self.name = name
        self.is_active = is_active
    
redBall = Pokeball(10, 'RedBall','SuperBall', True )

print(f'Nombre de redBall: {redBall.name}')

# Clase que no necesita parametros, pero con una propiedad predefinida
class PokeballInit:
    def __init__(self) -> None:
        self.size = 10
        self.type = 'RedBall'
        self.name = 'SuperBall'
        self.is_active = True
    
redBall = PokeballInit()

print(f'Nombre de redBall: {redBall.name}')

# Clase sin parametros, pero con una propiedad predefinida 2
class PokeballFunct:
    def __init__(self) -> None:
        self.description = f'{10} RedBall SuperBall {True}'
    
redBall = PokeballFunct()

print(f'Description: {redBall.description}')

# Clase sin parametros, con funcion
class PokeballFunct:
    def __init__(self) -> None:
        self.description = 'RedBall - SuperBall'
    
    def lanzar (self):
        print(f'{self.description} esta disponible en la tienda')
    
redBall = PokeballFunct()
redBall.lanzar()


# Clase parametros por defecto
class PokeballDefault:
    def __init__(self, size = 10, type = 'MegaBall', name = 'SuperMegaBall', is_active = False,) -> None:
        self.size = size
        self.type = type
        self.name = name
        self.is_active = is_active

    def lanzar (self):
            if self.is_active == False:
                text = 'no esta activa'
            else:
                text = 'se rompio'
            print(f'Usted lanzo una {self.name}, pero esta {text}')

    
pokeball = PokeballDefault()

print(f'Default ball {pokeball.name}')
pokeball.lanzar()
pokeball.name = 'BlandexBall'
pokeball.is_active = True
print(f'New ball name => {pokeball.name}')
pokeball.lanzar()



# Clase parametros privados
class PokeballPrivate:
    def __init__(self, size = 10, type = 'MegaBall', name = 'SuperMegaBall', is_active = False,) -> None:
        self.size = size
        self.__type = type
        self.name = name
        self.is_active = is_active

    def lanzar (self):
            if self.is_active == False:
                text = 'no esta activa'
            else:
                text = 'se rompio'
            print(f'Usted lanzo una {self.name}, pero esta {text}')
    def get_type (self):
        return self.__type

    
pokeball = PokeballPrivate()
print(f'Default ball {pokeball.get_type()} type')


