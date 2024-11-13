# Condicionales
puerta = True

if puerta:
    print('La puerta esta abierta')
    
puerta = False
print('Hay mas puertas')
# IF - ELSE
if puerta == True:
    print('La puerta esta abierta')
else:
    print('La puerta fue cerrada')
    
print('Las puertas fueron cerradas')

# IF - ELIF - ELSE 
if True and False:
    print('Nothing Here')
elif True and True:
    print('Hey elif')
else:
    print('Nothing Here')

# AND / OR
if True and True:
    print('Condition AND')
if False or True:
    print('Condition OR')
    
# Check doble
if (True and False) or (True and True):
    print('Hey doble check')

# Empty String
if "": 
    print('Nothing Here')

# Negado
if not "":
    print('String Printed not')

# Check string
if "abc" == 'abc':
    print('String Printed ==')

