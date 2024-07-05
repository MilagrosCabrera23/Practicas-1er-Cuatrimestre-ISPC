# 1- ¿Cual es la forma de importacion recomendada? Esta la forma mas comun es import, luego sigue import module,  La operación de búsqueda de la instrucción import se define como una llamada a la función __import__(), con los argumentos adecuados. El valor retornado de __import__() se utiliza para realizar la operación de enlace de nombre de la instrucción import. importlib
# El módulo importlib proporciona una API enriquecida para interactuar con el sistema de importación. Por ejemplo importlib.import_module() proporciona una API recomendada y más sencilla que la integrada __import__() para invocar la maquinaria de importación. 


#2 - ¿ Se puede construir nuestro programa primcipal sin especificar -main-?Es una buena practica?
# Sí, en Python es posible construir un programa principal sin especificar una función llamada main(). Sin embargo, es una práctica común y recomendada en Python definir una función main() que actúe como punto de entrada del programa. Esto proporciona claridad y estructura al código, especialmente en programas más grandes o complejos.


# 3 - ¿Si estamos poniendo toda la logica en un mismo archivo? Puedo definir las funciones luego del codigo especificado como main?
# En Python puedes definir las funciones en cualquier lugar del archivo, ya sea antes o después de la función main() o del bloque de código principal. Python es un lenguaje interpretado, lo que significa que el orden en el que defines las funciones dentro de un archivo no importa siempre y cuando las funciones estén definidas antes de que intentes llamarlas.


