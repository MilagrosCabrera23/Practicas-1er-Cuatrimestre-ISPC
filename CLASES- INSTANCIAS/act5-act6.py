# 5. Agenda de Contactos. Crea una clase Contacto que almacene información
# sobre personas en una agenda. Implementa los métodos _str_ y
# _setitem_ para mostrar detalles del contacto y modificar sus atributos (por
# ejemplo, número de teléfono)

class Contacto: 
    def __init__(self,nombre,email,telefono):
        self.nombre = nombre, 
        self.email = email,
        self.telefono = telefono
        
def __str__(self):
    return (f"Nombre: {self.nombre}, Email: {self.email}, Telefono: {self.telefono}")

def __getitem__(self,key):
    if key == 'nombre':
        return self.nombre
    elif key == 'email':
        return self.email
    elif key == 'telefono':
        return self.telefono
    else: 
     raise ValueError("Valor incorrecto")
 
 #inicializar la clase
contacto1 = Contacto('lucia', 'luci23@gmail.com', '351402741')
print(contacto1)


# 6. Instrumentos Musicales. Crea una clase base llamada Instrumento
# con métodos como tocar() y afinar(). Luego, crear subclases para representar
# diferentes instrumentos como Guitarra, Piano y Flauta. Implementa métodos
# de manera diferente en cada subclase para simular la ejecución y la afinación
# de cada instrumento.

class Instrumento:
    def tocar(self): 
       raise NotImplementedError("Este método debe ser implementado por la subclase")
    def afina(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")
    
class Guitarra(Instrumento): 
    def tocar(self):
        return("Tocando la guitarra:strum strum")
    
    def afinar(self):
        return("Afinando la guitarra,ajustando cuerdas")
    
class Piano(Instrumento):       
    def tocar(self):
        return("Tocando el piano:plink plonk")
    
    def afinar(self):
        return("Afinando el piano,ajustando tensiones de las cuerdas")
     
class Flauta(Instrumento): 
   def tocar(self):
        return("Tocando el piano:plink plonk")
    
   def afinar(self):
        return("Afinando el piano,ajustando tensiones de las cuerdas")
    
guitarra1 = Guitarra()  
piano1 = Piano()   
flauta1 = Flauta()

print(guitarra1.tocar())
print(guitarra1.afinar())

print(piano1.tocar())
print(piano1.afinar())

print(flauta1.tocar())
print(flauta1.afinar())