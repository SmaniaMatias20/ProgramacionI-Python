from Funciones import *

# Matias Smania 1D

while True:
    print("""
        ---Menu de opciones---
        1 - Calcular el area de un circulo.
        2 - Determinar numero par o impar. 
        3 - Sumar todos los elementos de una lista.
        4 - Determinar el maximo entre tres numero.
        5 - Invertir cadena.
        6 - Ordenar palabras alfabeticamente.
        7 - Calcular la potencia de un numero.
        8 - Devolver solo los numeros pares de una lista.
        9 - Calcular el producto de una lista de numeros.
        10 - Determinar si una cadena es un palindromo.
        11 - Salir   
        """)
    opcion = input("Eliga una opcion: ")

    while not opcion.isdigit() or opcion == None or int(opcion) < 1 or int(opcion) > 11:
        opcion = input("Eliga la opcion correctamente: ")

    opcion = int(opcion)

    match opcion:
        case 1:
            radio = input("Ingrese el radio") 
            area = calcularArea(radio)
            print(f"El area del circulo es: {area}")
        case 2:
            numero = input("Ingrese un numero: ")
            calcularNumeroPar(numero)
        case 3:
            lista_de_numeros = [10,5,9,7,6]
            suma = sumarListaDeNumeros(lista_de_numeros)
            print(f"El resultado de la suma de todos los numeros es: {suma}")
        case 4:
            primer_numero = input("Ingrese el primer numero: ")
            segundo_numero = input("Ingrese el segundo numero: ")
            tercer_numero = input("Ingrese el tercer numero: ")
            numero_maximo = numeroMaximo(primer_numero, segundo_numero, tercer_numero)
            print(f"El numero maximo es: {numero_maximo}")
        case 5:
            cadena = input("Ingrese la cadena: ")
            invertirCadena(cadena)
        case 6:
            lista_de_palabras = ["colectivo", "avion", "auto", "tren"]
            lista_de_palabras_ordenadas = listaDePalabrasOrdenadas(lista_de_palabras)
            print(lista_de_palabras_ordenadas)
        case 7:
            base = input("Ingrese la base: ")
            exponente = input("Ingrese el exponente: ")
            potencia = calcularPotencia(base, exponente)
            print(f"El resultado de la potencia es: {potencia}") 
        case 8:
            lista_de_numeros = [2,5,3,6,8,0,10,9,1]
            lista_pares = obtenerNumerosPares(lista_de_numeros)
            print(f"Los numeros pares de la lista son: {lista_pares}")
        case 9:
            lista_de_numeros = [2,5,3,6,8,4,10,9,1]
            producto = calcularProducto(lista_de_numeros)
            print(f"El producto de toda la lista es: {producto}")
        case 10:
            cadena = input("Ingrese la cadena: ")
            cadenaPalindromo(cadena)
        case _:
            break