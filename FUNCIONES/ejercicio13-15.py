# 13- Escribe una funcion que tome una cantidad variable de cadenas y las concatene en una sola cadena. Ej: HOLA MUNDO.
def cadenas_concatenadas(*args):
    concatenacion = ""
    for cadena in args:
        concatenacion += cadena
    return concatenacion


resultado = cadenas_concatenadas("hola", " ", "mun", "do")
print(resultado)

# 14- Escribe una funcion que muestre la cantidad de argumentos con nombre enviados.
def nombres_enviados(**kwargs): 

    print("Los nombres enviados son:", {len(personas)})
    
personas = ("Leon", "Luna", "Francisco", "Luciana", "Javier", "Fiamma")
    
print("Estos son: ", personas)

nombres_enviados()


# 15- Escribe una funcion que calcule el promedio de una cantidad variable de numeros. 

def promedio(*args): 
    if not args:
        return 0  # Devuelve 0 si no se proporcionan argumentos
    
    promedio_total = sum(args) / len(args)
    return promedio_total

# Ejemplo de uso
numeros_promedio = (1, 2, 13, 24, 35, 46, 57, 68, 79, 80) 
resultado = promedio(*numeros_promedio)

print(f"El promedio es:", resultado)