# 1- Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el
# número con los dígitos en orden inverso:

entero_ingresado = int(input("Ingrese un entero de 3 digitos"))
entero_cadena = str(entero_ingresado)
entero_convertido = entero_cadena[::-1]

print("El numero de tres digitos de forma reversa es_ ",entero_convertido)                     
                       
                       
# 2- Escriba un programa que pregunte al usuario la hora actual t del reloj y un número
# entero de horas h, que indique qué hora marcará el reloj dentro de h horas:
    
hora_actual = float(input("Ingrese la hora actual"))
numero_horas = int(input("Ingrese un numero de horas"))
hora_posterior = (hora_actual + numero_horas) % 24

print("En:", numero_horas,"horas del reloj marcara las:",hora_posterior)

# 3- Escribir un programa que pida al usuario un número entero y muestre por pantalla si
# es un número primo o no.

def numeroPrimo(numero): 
    # Verifica si un número es menor o igual a 1, en cuyo caso no es primo y retorna False.
    if numero <=1: 
        return False
     # Itera desde 2 hasta la raíz cuadrada del número (más eficiente que iterar hasta el número mismo). Si encuentra algún divisor en este rango, significa que el número no es primo y retorna False
    for i in range(2, int(numero**0.5)+ 1):
        # Si el bucle termina sin encontrar divisores, el número es primo y retorna True
        if numero % i == 0:
            return False
    return True

ingresoNumero = int(input("Ingrese un numero"))

if numeroPrimo(ingresoNumero):
    print(f"{ingresoNumero} es un numero primo")
else:
    print(f"{ingresoNumero} es un numero impar")
    
    
# 4- Tiempo de viaje. Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él
# tiene la duración en minutos de cada uno de los tramos del viaje.
# Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y
# entregue como resultado el tiempo total de viaje en formato horas:minutos.
# El programa deja de pedir tiempos de viaje cuando se ingresa un 0.

Cantidad_tramos = int(input("Ingrese la cantidad de intervalos que realizo en su viaje"))

tiempo_total = 0

for _ in range(Cantidad_tramos): 

    tramo = int(input("Ingrese el primer intervalo del viaje"))
    tiempo_total += tramo
   
    if tramo == 0:
       break

horas = tiempo_total // 60
minutos = tiempo_total % 60

print(f"El tiempo del viaje es:", horas ,"horas y", minutos,"minutos")
    

# 5- Cuando la Tierra completa una órbita alrededor del Sol, no han transcurrido
# exactamente 365 rotaciones sobre sí misma, sino un poco más. Más precisamente, la
# diferencia es de más o menos un cuarto de día.
# Para evitar que las estaciones se desfasen con el calendario, el calendario juliano
# introdujo la regla de introducir un día adicional en los años divisibles por 4 (llamados
# bisiestos), para tomar en consideración los cuatro cuartos de día acumulados.
# Sin embargo, bajo esta regla sigue habiendo un desfase, que es de aproximadamente
# 3/400 de día.
# Para corregir este desfase, en el año 1582 el papa Gregorio XIII introdujo un nuevo
# calendario, en el que el último año de cada siglo dejaba de ser bisiesto, a no ser que
# fuera divisible por 400.
# Escriba un programa que indique si un año es bisiesto o no, teniendo en cuenta cuál era
# el calendario vigente en ese año:

def es_bisiesto(año):
    
    if año < 1582:
     return año % 4 == 0
    else:
        if año % 400 == 0: 
            return True
        
        elif año % 100 == 0: 
            return False
        
        else: 
            return False


año = int(input("Ingrese el año en que se encuentra"))

if es_bisiesto(año): 
    print(año, "el año es bisiesto")
else:
    print(año,"el año no es bisiesto")
    
    