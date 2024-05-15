from Data_stark import *
# Objetos de primera clase

# Funciones...
#   Puede asignarse a una variable.
#   Puede retornarse desde una funcion.
#   Puede pasarse como parametro de una funcion.


# Apuntamos la variable mi_funcion a la misma direccion de memoria que la funcion sumar.
# def sumar(a, b):
#     print(a + b)

# mi_funcion = sumar
# mi_funcion(5, 7)



# def sumar(a, b):
#     return a + b
    
# def restar(a, b):
#     return a - b

# def multiplicar(a, b):
#     return a * b

# def dividir(a, b):
#     return a / b

# def calcular(a, b, que_calcula):
#     resultado = que_calcula(a, b)
#     print(resultado)

# calcular(5, 7, sumar)
# calcular(3, 5, multiplicar)

# Funciones Lambda ---> Son anonimas, no tienen nombre. Se crea, se ejecuta y se elimina de la memoria.
# funcion = lambda a, b: (a+b) / 2
# resultado = funcion(5, 9)

# print(resultado)

# Map

# lista = [5,9,7,5,3,4,1,3,6,9,0,8]

# def duplicar(lista):
#     lista_modificada = []
#     for numero in lista:
#         x = numero * 2
#         lista_modificada.append(x)
#     return lista_modificada

# lista_duplicada = duplicar(lista)


# lista_duplicada = list(map(lambda item: item * 2, lista))
# print(lista_duplicada)

# for numero in lista_duplicada:
#     print(numero)

# colores = set(map(lambda heroe: heroe["color_ojos"], lista_personajes))

# for color in colores:
#     print(color)

# Filter

# lista = [5,9,7,5,3,4,1,3,6,9,0,8]

# pares = list(filter(lambda numero: numero % 2 == 0 and numero != 0, lista))

# for numero in pares:
#     print(numero)


# Filtrar por genero.
# masculino = list(filter(lambda heroe: heroe["genero"] == "M", lista_personajes))
# print(len(masculino))

# Reduce (funcion de fila unica).
from functools import reduce

lista = [5,9,7,5,3,4,1,3,6,9,0,8]

total = reduce(lambda anterior, actual: anterior + actual, lista, 0)
maximo = reduce(lambda max, actual: max if max > actual else actual, lista, 0)

print(total)
print(maximo)








