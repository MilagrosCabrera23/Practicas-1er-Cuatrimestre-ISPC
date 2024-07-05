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
    
    # Diccionarios de conversión
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'
}

inverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}

# Función para convertir texto a Morse
def text_to_morse(text):
    text = text.upper()
    return ' '.join(morse_code_dict[char] for char in text if char in morse_code_dict)

# Función para convertir Morse a texto
def morse_to_text(morse):
    return ''.join(inverse_morse_code_dict[char] for char in morse.split(' ') if char in inverse_morse_code_dict)

# Función para detectar y convertir
def auto_convert(input_string):
    if set(input_string) <= set('.- /'):
        return morse_to_text(input_string)
    else:
        return text_to_morse(input_string)

# Ejemplos de uso
natural_text = "Hola Mundo"
morse_code = ".... --- .-.. .- / -- ..- -. -.. ---"

print("Texto a Morse:", text_to_morse(natural_text))
print("Morse a Texto:", morse_to_text(morse_code))
print("Conversión automática (Texto a Morse):", auto_convert(natural_text))
print("Conversión automática (Morse a Texto):", auto_convert(morse_code))
