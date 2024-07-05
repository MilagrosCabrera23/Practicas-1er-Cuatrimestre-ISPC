# 12- De lo anterior,podemos inferir que podemos especificar funciones que admitan argumentos unicamente posicionales o bien funciones que admitan docuemntos unicamente con palabras claves. Escribe un ejemplo de cada uno y luego intenta romper la regla especificada en la definicion de la funcion. 

def funcion_palabras_clave(*, x, y):
    print(f"x: {x}, y: {y}")

# Llamada correcta usando solo argumentos con nombre
funcion_palabras_clave(x=10, y=20)

# Intento de romper la regla usando argumentos posicionales (esto causará un error)
try:
    funcion_palabras_clave(10, 20)
except TypeError as e:
    print(f"Error: {e}")
    
    
def funcion_posicional(a, b, /):
    print(f"a: {a}, b: {b}")

# Llamada correcta usando solo argumentos posicionales
funcion_posicional(1, 2)

# Intento de romper la regla usando argumentos con nombre (esto causará un error)
try:
    funcion_posicional(a=1, b=2)
except TypeError as e:
    print(f"Error:{e}")

