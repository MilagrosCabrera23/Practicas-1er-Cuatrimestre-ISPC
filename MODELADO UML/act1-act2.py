# 1- Considera un sistema de gestión de biblioteca dónde las
# instancias posibles son los Libros. Ej. “El principito”. Modela la clase Libro
# utilizando los símbolos definidos por el Diagrama de Clases UML
# identificando atributos, métodos y sus correspondientes modificadores de
# acceso.

#RESPUESTA/IMG DEL MODELADO:
# https://lucid.app/lucidchart/9e89048d-070b-45bd-8f05-1131ad84de9f/edit?invitationId=inv_b9c8a111-aded-476f-95f3-2effa052c38f&page=HWEp-vi-RSFO

#2- Desafío. ¿Es posible heredar de múltiples clases base? Investiga e
# identifica ejemplos.

# En Python, la herencia múltiple es soportada de manera directa y se puede implementar fácilmente.Por ej: 
class A:
    def method(self):
        return "Method from A"

class B(A):
    def method(self):
        return "Method from B"

class C(A):
    def method(self):
        return "Method from C"

class D(B, C):
    pass

d = D()
print(d.method())  # Salida: Method from B
print(D.mro())  # Muestra el orden de resolución de métodos: [D, B, C, A, object]
