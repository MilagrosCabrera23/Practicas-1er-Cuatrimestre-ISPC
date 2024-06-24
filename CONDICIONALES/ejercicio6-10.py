# 6- Escribir un programa que pida al usuario un número entero y muestre por pantalla un
# triángulo rectángulo como el de más abajo con tantos renglones como indique el
# usuario.

ingreso_numero = int(input("Ingrese un numero entero"))
for i in range(1,ingreso_numero + 1):
    print("*" * i)


# 7- La secuencia de Collatz de un número entero se construye de la siguiente forma:
# ● si el número es par, se lo divide por dos;
# ● si es impar, se le multiplica tres y se le suma uno;
# ● La sucesión termina al llegar a uno.
# Desarrolle un programa que entregue la secuencia de Collatz de un número entero:

def collatz(numero):
    secuencia = [3]
    
    while numero != 1:
        #si es divisible por 2, es par
        if numero % 2 == 0:
            numero //= 2
               #si NO es divisible por 2, es IMPAR
        else:
            numero = numero * 3 + 1
            secuencia.append(numero)
           
    return  secuencia
             
numero = int(input("Ingrese un numero que desee la secuencia de collatz")) 
  
secuencia_collatz = collatz(numero) 
print("La secuencia de Collatz para el numero", numero, "es:")
print(secuencia_collatz)


# 8-  Una máquina de alimentos tiene productos de tres tipos, A, B y C, que valen
# respectivamente $270, $340 y $390. La máquina acepta y da de vuelto monedas de $10, $50 y $100.
# Escriba un programa que pida al usuario elegir el producto y luego le pida ingresar las
# monedas hasta alcanzar el monto a pagar. Si el monto ingresado es mayor que el precio
# del producto, el programa debe entregar las monedas de vuelto, una por una.

def elegir_producto():
  precios = {1:270,2:340,3:370}
  
  producto = input("Elija cual de estas 3 opciones desea: 1(A vale 270), 2(B, cuesta 340), 3(C vale 390))")

if producto not in precios: 
  print("El valor ingresado es invalido,vuelva a ingresar ")
  
  producto = input("Elija cual de estas 3 opciones desea: 1(A vale 270), 2(B, cuesta 340), 3(C vale 390))")
  
precio_producto = precios[producto]
  
monto_pagar = int(input("Escriba el valor que desea pagar segun el producto elegido con monedas de 10, 50 y 100"))


while monto_pagar < precio_producto:
  moneda = int(input("Ingrese una moneda (10, 50, 100): "))
  
  if moneda in [10,50,100]:
    monto_pagar += moneda
    
  print(f"Monto pagado hasta ahora: {monto_pagar}")
else:
            print("Moneda inválida, intente nuevamente.")

vuelto = monto_pagar - precio_producto
monedas = [10,50,100]
vuelto_moedas = []

if vuelto_monedas: 
  print("El vuelto es de $:", sum(vuelto_en_monedas)) 
else:
    print("No hay vuelto que darle,gracias por su compra")

elegir_producto()

# 9 - Anagrama. Escribe una función que reciba dos palabras y retorne
# verdadero o falso según sean o no anagramas.
# ● Un Anagrama consiste en formar una palabra reordenando TODAS las letras de
# otra palabra inicial.
# ● NO hace falta comprobar que ambas palabras existen.
# ● Dos palabras exactamente iguales no son anagrama.

def es_anagrama(cadena1,cadena2): 
    
  if len(cadena1) != len(cadena2):
    #    Si las longitudes son diferentes, no pueden ser anagramas
      return False 
  
        # Solicitar al usuario que ingrese una cadena de texto
cadena1 = input("Ingrese una cadena de texto: ") 
cadena2 = input("Ingrese la segunda cadena de texto: ")
    
if cadena1 == cadena2:
        print("La cadena ingresada es verdadero, si es un anagrama")
else:
        print("La cadena ingresada es falsa, No es un anagrama")

    
# 10- Torre y Alfil. Un tablero de ajedrez es una grilla de ocho filas y ocho columnas,
# numeradas de 1 a 8. Dos de las piezas del juego de ajedrez son el alfil y la torre. El alfil se
# desplaza en diagonal, mientras que la torre se desplaza horizontal o verticalmente. Una
# pieza puede ser capturada por otra si está en una casilla a la cual la otra puede
# desplazarse:
# Escriba un programa que reciba como entrada las posiciones en el tablero de un alfil y de
# una torre, e indique cuál pieza captura a la otra:

def capturar_piezas(alfil,torre):
  # Extraer las coordenadas de fila y columna para el alfil y la torre
    alfil_fila, alfil_columna = alfil
    torre_fila,torre_columna = alfil
  
   # Verificar si el alfil y la torre están en la misma fila, columna o diagonal
  #  comprueba si el alfil y la torre están en la misma fila
    if alfil_fila == torre_fila or alfil_columna == torre_columna or abs(alfil_fila - torre_fila) == abs(alfil_columna - torre_columna):
        return "Ambas piezas se pueden capturar mutuamente."
      
      # Si las piezas no están en la misma fila, columna o diagonal, se verifica si están en casillas de colores opuesto
    elif (alfil_fila + alfil_columna) % 2 == (torre_fila + torre_columna) % 2:
        return "El alfil captura a la torre."
      
    else:
        return "La torre captura al alfil."
   
   # Obtener las posiciones del alfil y la torre del usuario
alfil_posicion = tuple(map(int, input("Ingrese la posición del alfil (fila columna), separadas por espacio: ").split()))

torre_posicion = tuple(map(int, input("Ingrese la posición de la torre (fila columna), separadas por espacio: ").split()))

   # Determinar qué pieza captura a la otra
resultado = captura_piezas(alfil_posicion, torre_posicion)
print(resultado)

