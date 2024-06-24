# 7:Escribe un programa basado en la programación orientada a objetos (POO) con
# herencia simple en base al video juego Mario Bros:
#  Crear una clase base llamada “Personaje”: esta clase contendrá los atributos
# y métodos comunes a todos los personajes del juego. Por ej. los atributos
# podrían ser nombre, vidas y poder. Los métodos podrían ser: mover, saltar y
# caer.
# 2. Crea clases derivadas para cada personaje específico. Estas clases heredarán
# de la clase base “Personaje” y podrán tener atributos y métodos adicionales.
# Por ej. la clase Mario podría tener un método adicional lanzar_fuego()
# mientras que la clase Luigi podría tener un método adicional usar_hongo().
# 3. Crea clases base para los enemigos. Esta clase contendrá los atributos y
# métodos comunes a todos los enemigos. Por ejemplo, los métodos podrían ser
# tipo, daño y, los métodos podrían ser mover, atacar, etc.
# 4. Crear clases derivadas de la clase enemigo. Estas clases heredarán de la clase
# base “Enemigo” y podrán tener atributos y métodos adicionales. Por ej. la
# clase “Koopa Troopa” podría tener un método adicional usar_casco(),
# mientras que la clase “Goomba” podría tener un método esconder()
# Nota: Para la implementación de los métodos simplemente imprime en pantalla un
# texto que explique lo que haría el personaje.

# Definición de la clase base Personaje
class Personaje:
    def __init__(self, nombre, vidas, poder):
        self.nombre = nombre
        self.vidas = vidas
        self.poder = poder

    def saltar(self):
        print(f"{self.nombre} está saltando.")

    def moverse(self):
        print(f"{self.nombre} se está moviendo.")

    def caer(self):
        print(f"{self.nombre} está cayendo.")

# Definición de las clases Mario y Luigi, derivadas de Personaje
class Mario(Personaje):
    def lanzar_fuego(self):
        print(f"{self.nombre} lanza una bola de fuego!")

class Luigi(Personaje):
    def usar_hongo(self):
        print(f"{self.nombre} usa un hongo para crecer!")

# Definición de la clase base Enemigo
class Enemigo:
    def __init__(self, tipo, vida, daño):
        self.tipo = tipo
        self.vida = vida
        self.daño = daño

    def mover(self):
        print(f"{self.tipo} se está moviendo.")

    def atacar(self):
        print(f"{self.tipo} está atacando.")

# Definición de las clases KopaTropa y Goomba, derivadas de Enemigo
class KopaTroopa(Enemigo):
    def usar_casco(self):
        print(f"{self.tipo} usa su caparazón como defensa.")

class Goomba(Enemigo):
    def esconderse(self):
        print(f"{self.tipo} se esconde para protegerse.")

# Ejemplo de uso
if __name__ == "__main__":
    # Creando instancias de personajes
    mario = Mario("Mario", 3, "Super Saltador")
    luigi = Luigi("Luigi", 3, "Super Saltador")

    # Probando métodos específicos de Mario y Luigi
    mario.lanzar_fuego()
    luigi.usar_hongo()

    # Creando instancias de enemigos
    koopa = KopaTroopa("Koopa Troopa", 1, "Medio")
    goomba = Goomba("Goomba", 1, "Bajo")

    # Probando métodos específicos de KopaTroopa y Goomba
    koopa.usar_casco()
    goomba.esconderse()
