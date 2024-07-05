# 4- Crear una funcion anonima que calcule el promedio de un arreglo de numeros enteros.
promedio = lambda arreglo:sum(arreglo) / len(arreglo)

#arreglo de numeros enteros
numeros= [2,35,41,56,98,100]

print(promedio(numeros))

# 5- Escribe una funcion anonima que calcule el factorial dado un numero entero.
# Esta es una expresión condicional que devuelve 1 si n es igual a 0.
# Si n no es 0, la función devuelve n multiplicado por el resultado de factorial(n - 1).

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
print(factorial(8))

# 6- Crea una funcion anonima que calcule que permita conocer si un numero es par. 

par = lambda a: a % 2 == 0 

# 7- Dado un arreglo de numeros enteros,crea una funcion anonima que retorne una lista con numeros pares.
# filter aplica la función lambda a cada elemento de arregl01 y crea un iterador que incluye solo aquellos elementos para los cuales la función lambda retorna True.
# Convierte el iterador resultante de filter en una lista.

arregl01 = [21,3,65,890,39,14]

pares =list(filter(lambda y: y % 2 == 0, arregl01 ))

print(pares)

# 8- Utiliza uan funcion lambda para elevar al cuadrado cada elemento de una lista de numeros.

numeros = [1,65,23,2,123,980,]

cuadrado = list(map(lambda x: x ** 2, numeros))
print(cuadrado)
