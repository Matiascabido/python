# Bucles / Loops / Ciclos

# While
stock = 0
print('While start')
while stock < 10:
    print('El stock llego a: ', stock)
    stock += 1
else: print('While end')

# Frenar while
while stock < 20:
    print('El stock llego a: ', stock)
    stock += 1
    if stock == 15:
        print('Ya son 15, stock lleno')
        break
    print('Rellenando...')


# For
bingo = [30, 40, 22, 15, 4, 0, 37, 97]
carton = (30, 30, 9, 5)
bola = {"tipo": 'bola', 'numero': 33}
numero = {'blanco', 'redondo'}

# List
for number in bingo:
    print(number)
 
# Tupla   
for number in carton:
    print(number)

# Set   
for number in numero:
    print(number)

# Dict
for number in bola:
    print(number)
else:
    print('no more bola')

# Break
for number in bola:
    if number == 'numero':
        print('termine...')
        break
else:
    print('temine el bucle')
    
# Continue
for number in bola:
    if number == 'numero':
        print('continuo...')
        continue
else:
    print('temine el bucle')