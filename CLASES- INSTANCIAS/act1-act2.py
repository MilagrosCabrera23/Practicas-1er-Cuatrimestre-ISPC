#Desafío. Intenta crear una clase Dado que cumpla los siguientes
# requerimientos:
# ● el dado debe tener un número de caras (por defecto 6)
# ● debe ser capaz de lanzarse y devolver un número aleatorio entre 1
# y el número de caras.
import random 

class Dado: 
    def _init_(self, caras=6):
        self.caras = caras
    
def lanzar(self): 
    #Devuelve un número aleatorio entre 1 y el número de caras del dado.
    return random.randint(1,self.caras)
    
    # Crear un dado con 6 caras (valor por defecto)
    dado1 = Dado()
    # Lanzar el dado y obtener un número entre 1 y 6
    print(dado1.lanzar())
    
    dado2 = Dado()
    print(dado2.lanzar())
    
    # 2. Conversor de Monedas. Crea una clase Moneda que permita la conversión
# entre monedas (ej. dólares a pesos). Implementa los métodos _str_ y
# _add_ para mostrar la cantidad convertida y sumar cantidades en
# diferentes monedas.

class Moneda:
    tasa_conversion = {
        'dolar': 21.4,
        'euro': 13.5,
        'libra': 45.1,
        'peso_mexicano': 30.9
    }
    
    def __init__(self, cantidad, tipo_moneda):
        self.cantidad = float(cantidad)  # Asegurar que cantidad sea un número flotante
        self.tipo_moneda = tipo_moneda.lower()

    def convertir_a(self, otra_moneda):
        otra_moneda = otra_moneda.lower()
        if self.tipo_moneda == otra_moneda:
            return Moneda(self.cantidad, self.tipo_moneda)
        else:
            tasa_origen = Moneda.tasa_conversion.get(self.tipo_moneda)
            tasa_destino = Moneda.tasa_conversion.get(otra_moneda)
            if tasa_origen is None or tasa_destino is None:
                raise ValueError(f"No hay tasa de cambio definida para {self.tipo_moneda} a {otra_moneda}")
            cantidad_en_pesos = self.cantidad * tasa_origen
            nueva_cantidad = cantidad_en_pesos / tasa_destino
            return Moneda(nueva_cantidad, otra_moneda)

    def __str__(self):
        return f"{self.cantidad:.2f} {self.tipo_moneda}"
    
    def __add__(self, otra):
        if self.tipo_moneda == otra.tipo_moneda:
            return Moneda(self.cantidad + otra.cantidad, self.tipo_moneda)
        else:
            otra_convertida = otra.convertir_a(self.tipo_moneda)
            return Moneda(self.cantidad + otra_convertida.cantidad, self.tipo_moneda)

# Ejemplo de uso
moneda1 = Moneda(30, 'libra')
print(moneda1)  # Salida: 30.00 libra

moneda2 = Moneda(100, 'euro')
print(moneda2)  # Salida: 100.00 euro

moneda3 = Moneda(900, 'peso_mexicano')
print(moneda3)  # Salida: 900.00 peso_mexicano

# Convertir y mostrar
moneda_convertida = moneda3.convertir_a('libra')
print(moneda_convertida)  # Salida aproximada dependiendo de las tasas de cambio

# Sumar monedas y mostrar
moneda_sumada = moneda1 + moneda2
print(moneda_sumada)  # Salida aproximada dependiendo de las tasas de cambio

