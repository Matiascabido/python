# Exceptions Handling
print('--- START ---')

# Fallando
try:
    print(1 + '5')
except:
    print('except: Something Went Wrong')
else:
    print('Else')
finally:
    print('Finaly')

print('--- Next ---')

# No fallo
try:
    print(2 + 5)
except:
    print('except: Something Went Wrong')
else:
    print('Else')
finally:
    print('Finaly')

print('--- Next ---')

# Tipo de errores
try:
    print(3 + '5')
except ValueError:
    print('except ValueError: Something Went Wrong')
except TypeError:
    print('except TypeError: Something Went Wrong')
    
print('--- Next ---') 

# Caputrando el error
try:
    print(4 + '5')
except TypeError as error:
    print(f'except TypeError: {error}')
    
print('--- Next ---') 

try:
    print(5 + '5')
except ValueError as error:
    print(f'except ValueError: {error}')
except Exception as error:
    print(f'except Exception: {error}')
    
print('--- END ---')