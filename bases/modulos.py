# Modulos

# Importar todo el modulo
import module

module.sum(1,3,4)
module.rest(1,3,4)

# Importar funcion especifica
from module import sum, rest

sum(1,3,4)
rest(1,3,4)

import math

print(math.pi)
print(math.sqrt(3))
print(math.pow(3, 3))

# Renombrar funcion importada
from math import pi as PI_VALUE

print(PI_VALUE)