# 3. Registro de Tareas. Crea una clase Tarea que almacene información sobre
# tareas pendientes. Implementa los métodos _str_ y _len_ para mostrar
# detalles de la tarea y contar cuántas tareas hay en la lista.

class Tareas:
    def __init__(self):
        self.lista_de_tareas = []

    def sumar_tareas(self, nombre, descripcion):
        tarea = {'nombre': nombre, 'descripcion': descripcion}
        self.lista_de_tareas.append(tarea)

    def __str__(self):
        if not self.lista_de_tareas:
            return 'No hay tareas pendientes.'
        return "\n".join(f"{tarea['nombre']}: {tarea['descripcion']}" for tarea in self.lista_de_tareas)

    def __len__(self):
        return len(self.lista_de_tareas)

# Ejemplo de uso
tareas_pendientes = Tareas()
tareas_pendientes.sumar_tareas("Ir al supermercado", "Comprar pan y leche")
tareas_pendientes.sumar_tareas("Lavar el coche", "Lavar el coche el sábado por la mañana")

# Mostrar detalles de las tareas
print(f"las tareas pendientes son:{tareas_pendientes}")  # Salida: Ir al supermercado: Comprar pan y leche\nLavar el coche: Lavar el coche el sábado por la mañana

# Contar cuántas tareas hay en la lista
print(len(f"hay:{tareas_pendientes}tareas pendientes"))  # Salida: 2


# 4. Baraja de Cartas. Crea una clase Carta que represente una carta de la baraja.
# Implementa los métodos _str_ y _getitem_ para mostrar la carta y
# acceder a sus atributos (por ejemplo, palo y valor)

class Carta:
    palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor
    
    def __str__(self):
        return f"{self.valor} de {self.palo}"
    
    def __getitem__(self, key):
        if key == 'palo':
            return self.palo
        elif key == 'valor':
            return self.valor
        else:
            raise KeyError(f"Clave {key} no válida. Las claves válidas son 'palo' y 'valor'")

# Crear y mostrar algunas cartas de ejemplo
carta1 = Carta('Diamantes', 'K')
print(carta1)  # Salida: K de Diamantes

carta2 = Carta('Tréboles', 'J')
print(carta2)  # Salida: J de Tréboles
