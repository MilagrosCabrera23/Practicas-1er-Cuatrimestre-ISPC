def determinar_signo(fecha_de_nacimiento):
    signo_del_zodiaco = {
        'Aries': (("Mar", 21), ("Abr", 19)),
        'Tauro': (("Abr", 20), ("May", 20)),
        'Géminis': (("May", 21), ("Jun", 20)),
        'Cáncer': (("Jun", 21), ("Jul", 22)),
        'Leo': (("Jul", 23), ("Ago", 22)),
        'Virgo': (("Ago", 23), ("Sep", 22)),
        'Libra': (("Sep", 23), ("Oct", 22)),
        'Escorpio': (("Oct", 23), ("Nov", 21)),
        'Sagitario': (("Nov", 22), ("Dic", 21)),
        'Capricornio': (("Dic", 22), ("Ene", 19)),
        'Acuario': (("Ene", 20), ("Feb", 18)),
        'Piscis': (("Feb", 19), ("Mar", 20))
    }
    
    meses = {
        "Ene": 1, "Feb": 2, "Mar": 3, "Abr": 4, 
        "May": 5, "Jun": 6, "Jul": 7, "Ago": 8, 
        "Sep": 9, "Oct": 10, "Nov": 11, "Dic": 12
    }
    
    _, mes, dia = fecha_de_nacimiento

    for signo, (inicio, fin) in signo_del_zodiaco.items():
        mes_inicio, dia_inicio = inicio
        mes_fin, dia_fin = fin
        
        # Convertir a formato (mes, dia) en números  
        mes_inicio = meses[mes_inicio]
        mes_fin = meses[mes_fin]
        
        # Verificar si la fecha está en el rango  
        if (mes_inicio < mes < mes_fin) or \
           (mes == mes_inicio and dia >= dia_inicio) or \
           (mes == mes_fin and dia <= dia_fin):
            return signo
    
    return None

# Ejemplo de uso: 
fecha_de_nacimiento = (2000, 5, 19)
print(determinar_signo(fecha_de_nacimiento))  # Debería imprimir 'Tauro'


# 15- Código Morse. Crea un programa que sea capaz de transformar texto natural a
# código morse y viceversa.
# Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
# ● En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos
# espacios entre palabras " ".
# ● El alfabeto morse soportado será el mostrado en
# https://es.wikipedia.org/wiki/Código_morse
    
    