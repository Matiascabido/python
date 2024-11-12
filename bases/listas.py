# Listas
hero = []
enemy = list()


# Tipo lista
print('HERO:', type(hero)) 
print('ENEMY:', type(enemy))

# Listas
print('HERO:', hero)
print('ENEMY:', enemy)

# Tamaño de las listas
print('HERO_SIZE:', len(hero)) 
print('ENEMY_SIZE:', len(enemy))

# Agregar a listas
hero = ['DeadPool', 38, 'Speederman', 38, 'Doctor Strange', 48]
enemy.append('Loky')
enemy.append(90)

# Insertar un elemento en la lista en una posicion especifica
enemy.insert(0, 'Mabel')
print('ENEMY:', enemy)


# Remueve el primero que encuentra
enemy.remove('Mabel')
print('ENEMY:', enemy)

enemy.insert(0, 'Mabel')
print('ENEMY:', enemy)

# Remueve el ulitmo elemento de la lista
enemy.pop()
print('ENEMY_POP:', enemy)

# Retorna el elemento eliminado
enemy.insert(0, 'Mabel')
print('Return deleted item', enemy.pop())

# Remueve un elemento determinado de la lista
enemy.insert(0, 'Mabel')
del enemy[0]
print('ENEMY_DEL:', enemy)

# Listas
print('HERO:', hero)
print('ENEMY:', enemy)

# Tamaño de las listas
print('HERO_SIZE:', len(hero)) 
print('ENEMY_SIZE:', len(enemy))


# Acceder a listas
print(hero[0]) # DeadPool
print(hero[-1]) # Doctor Strange AGE = 48

# Cantidad de veces de un mismo valor
print('Hero with 38: ', hero.count(38))
print('How many Spidermans: ', hero.count('Speederman'))
print('How many Batmans: ', hero.count('Batman'))

# Deconstruccion de una lista (siempre es necesario deconstruir todos los elementos)
deadpool, deadpool_age, spiderman, spiderman_age, doctor_strange, doctor_strange_age = hero

print('Hero 1: ', deadpool)
print('Hero age: ', deadpool_age)
print('Hero 2: ', spiderman)
print('Hero age: ', spiderman_age)
print('Hero 3: ', doctor_strange)
print('Hero age: ', doctor_strange_age)

# Concatenar listas
print('Movie: ', hero + enemy)

# Copy
dead_heros = hero.copy()

hero.clear()
print('HEROES_VIVOS: ', hero)
print('HEROES_MUERTOS: ', dead_heros)

# Reversa
dead_heros.reverse()
print('LISTA AL REVEZ: ', dead_heros)

# Orden
power = [10, 1, 24, 55, 8]
power.sort()
print('LISTA SORT: ', power)

# Sublist
print(power[1:3])
