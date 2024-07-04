# 11- Piedra, papel y tijera. En cada ronda del juego del cachipún, los dos competidores
# deben elegir entre jugar tijera, papel o piedra.
# Las reglas para decidir quién gana la ronda son: tijera le gana a papel, papel le gana a
# piedra, piedra le gana a tijera, y todas las demás combinaciones son empates.
# El ganador del juego es el primero que gane tres rondas.
# Escriba un programa que pregunte a cada jugador cuál es su jugada, muestre cuál es el
# marcador después de cada ronda, y termine cuando uno de ellos haya ganado tres
# rondas. Los jugadores deben indicar su jugada escribiendo tijera, papel o piedra.

import random

def obtener_jugada(numero_jugador):
    jugada = input(f"Jugador {numero_jugador}, elige tijera, papel o piedra: ").strip().lower()
    while jugada not in ["tijera", "papel", "piedra"]:
        print("Jugada no válida. Por favor, elige tijera, papel o piedra.")
        jugada = input(f"Jugador {numero_jugador}, elige tijera, papel o piedra: ").strip().lower()
    return jugada

def determinar_ganador(jugador1, jugador2):
    if jugador1 == jugador2:
        return "Empate"
    elif (jugador1 == "tijera" and jugador2 == "papel") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "piedra" and jugador2 == "tijera"):
        return "Jugador 1"
    else:
        return "Jugador 2"

def jugar():
    marcador = [0, 0]
    rondas = 0

    while max(marcador) < 3:
        
#         \n: Añadirá una nueva línea antes del texto.
# rondas + 1: Evaluará 0 + 1, que es 1, así que imprimirá 1.
        print("\n--- Ronda", rondas + 1, "---")
        
        # Obtener jugadas de los jugadores
        jugada_jugador1 = obtener_jugada(1)
        jugada_jugador2 = obtener_jugada(2)
        
        # Determinar ganador de la ronda
        ganador = determinar_ganador(jugada_jugador1, jugada_jugador2)
        
        if ganador == "Jugador 1":
            marcador[0] += 1
        elif ganador == "Jugador 2":
            marcador[1] += 1
        
        # Mostrar resultado de la ronda
        print(f"Jugador 1 eligió: {jugada_jugador1}")
        print(f"Jugador 2 eligió: {jugada_jugador2}")
        print(f"Resultado de la ronda: {ganador}")
        print(f"Marcador: Jugador 1 - {marcador[0]}, Jugador 2 - {marcador[1]}")
        
        rondas += 1
        
    # Determinar ganador del juego
    if marcador[0] == 3:
        print("¡Jugador 1 ha ganado el juego!")
    else:
        print("¡Jugador 2 ha ganado el juego!")

# Llamar a la función principal para iniciar el juego
if __name__ == "__main__":
    jugar()

# 12- Torneo de Tenis. Escriba un programa para simular un campeonato de tenis.
# Primero, debe pedir al usuario que ingrese los nombres de ocho tenistas. A continuación,
# debe pedir los resultados de los partidos juntando los jugadores de dos en dos. El
# ganador de cada partido avanza a la ronda siguiente.
# El programa debe continuar preguntando ganadores de partidos hasta que quede un
# único jugador, que es el campeón del torneo.

def pedir_nombres(): 
    nombres_tenistas = []
    
    for i in range(1,9):
        input(f"Ingrese el nombre del tenista{i}".strip())
        
    nombres_tenistas.append(nombre)

return nombres_tenistas

def pedir_resultados(nombres_tenistas):
    

# 13- El diccionario países asocia cada persona con el conjunto de los países que ha
# visitado:
#     Escriba una función cuantos_en_comun(a, b), que indique cuántos países en común han
# visitado la persona a y la persona b:
    paises = {
      "Juan": {"Argentina", "Brasil", "Croacia", "Japon"},
      "Leila": {"Francia", "Brasil", "Japon", "Alemania"}, 
      "Franco": {"Brasil", "Japon", "Inglaterra","Corea del Sur"}, 
      "Gisel":{"Suecia", "Francia", "Croacia", "Brasil"}
  }  

def cuantas_en_comun(a,b):
    if a not in paises or b not in paises: 
        return 0
    
     # Encuentra los países en común usando la intersección de conjuntos,Usa el método .intersection() de los conjuntos para encontrar los países comunes entre las dos personas.
    paises_comunes = paises[a].intersection(paises[b])
  
    
# Devuelve la longitud del conjunto resultante, que representa el número de países en común.
    return len(paises_comunes)

#Ejemplo: 
persona_a = "Juan"
persona_b = "Leila"

print(f"Países en común entre {persona_a} y {persona_b}: {cuantas_en_comun(persona_a, persona_b)}")


