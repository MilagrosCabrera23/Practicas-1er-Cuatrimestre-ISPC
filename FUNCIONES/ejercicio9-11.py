# 9- Crea una funcion para calcular el area de un triangulo. Si no se proporciona la altura asumimosuna altura de 1. 
def area_del_Triangulo(base,altura=1): 
    
    area =  (base * altura) / 2 
    return area

base = int(input("Ingrese la longitud de la base del triángulo: "))
     
altura = int(input("Ingrese la altura del triángulo (si no se proporciona, se asumirá una altura de 1): ") or 1)

if altura:
    altura = float(altura)
else:
    altura = 1
    
area = area_del_Triangulo(base, altura)

print(f"El area del triangulo es: {area}")


# 10- Crea una funcion para saludar con un mesnaje personalizado. Si no se proporciona el nombre asumimos invitado.
def saludar(): 
    saludo = input("Hola, bienvenidos a programacion")
    nombre = input("Ingrese su nombre o apodo:")
    
    if nombre: 
        print(f"{nombre}, Hoy no habra clases" )
    
    else:
        print("Bye")  

saludar()

# 11- Crea una funcion para proporcionar un porcentaje de descuento. Si no se proporciona el porcentaje asumimos el 10%.

def descuento():
    monto = float(input("Ingrese el monto que debe pagar"))
    
    porcentaje_descuento = (input("Ingrese el porcentaje de descuento (si no se proporciona, se asumirá el 10%): ") or 10)
    
    monto_descuento = monto * (1 - porcentaje_descuento / 100) 
    print(f"El monto a pagar con un {porcentaje_descuento}% de descuento es del {monto_descuento} ")
   
descuento()
    