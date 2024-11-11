# Operators

# /////////////////////////////////// #

x = 1
y = 10
z = 8


print(x == y) # igual que
x += 5
print(x) # valor de x mas valor definido y se almacena en x
x -= 5
print(x) # valor de x menos valor definido y se almacena en x
y *= 5
print(y) # valor de y multiplicado por valor definido y se almacena en x
y /= 5
print(y) # valor de y dividido por valor definido y se almacena en x
z %= 5
print(x) # valor de z modulus del valor definido y se almacena en x
z **= 5
print(x) # valor de z exponencial al valor definido y se almacena en x
z //= 5.5
print(x) # valor de z dividido flotantemente del valor definido y se almacena en x

# Concatenar operaciones matematicas
math_operations = x + y - z * x / z % 5
print(math_operations)

# Operadores comparativos
print(5 > 6)
print(5 < 6)
print(5 >= 6)
print(5 <= 6)
print(5 == 6)
print(5 != 6)

# Operacion de Orden alfabetico
print('HOLA' > 'MUNDO')
print('HOLA' < 'MUNDO')
print('HOLA' >= 'MUNDO')
print('HOLA' >= 'AUNDO') 
print('HOLA' <= 'MUNDO')
print('HOLA' == 'MUNDO')
print('HOLA' != 'MUNDO')
print('HOLA' != 'MUND')
print('HOLA' != 'HOLA')

# Operacion de Orden numerico
print(len('HOLA') > len('MUNDO'))
print(len('HOLA') < len('MUNDO'))
print(len('HOLA') >= len('AUNDO')) 
print(len('HOLA') <= len('MUNDO'))
print(len('HOLA') == len('MUNDO'))
print(len('HOLA') != len('MUNDO'))

# Operadores logicos
print( 3 > 4 and 'Hola' != 'Duck')
print( 3 > 4 or 'Hola' == 'Duck')
print( 3 < 4 and 'Hola' != 'Duck')
print( 3 < 4 or 'Hola' == 'Duck')
