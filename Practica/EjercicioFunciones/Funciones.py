# Punto 1
def calcularArea(radio: float):
    PI = 3.14  
    area = PI * (radio ** 2)
    
    return area

# Punto 2
def calcularNumeroPar(numero: float):
    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")

# Punto 3      
def sumarListaDeNumeros(lista_de_numeros: list):
    suma = 0
    for numero in lista_de_numeros:
        suma += numero
    
    return suma

# Punto 4
def numeroMaximo(primer_numero: float, segundo_numero: float, tercer_numero: float):
    numero_maximo = 0
    
    if primer_numero >= segundo_numero and primer_numero >= tercer_numero:
        numero_maximo = primer_numero
    elif segundo_numero >= primer_numero and segundo_numero >= tercer_numero:
        numero_maximo = segundo_numero
    else:
        numero_maximo = tercer_numero
    
    return numero_maximo

# Punto 5
def invertirCadena(cadena: str):
    print(cadena[::-1])

# Punto 6
def listaDePalabrasOrdenadas(lista_de_palabras: list):
    lista_de_palabras.sort()
    
    return lista_de_palabras

# Punto 7
def calcularPotencia(base: float, exponente: int):
    resultado = base ** exponente
    
    return resultado

# Punto 8
def obtenerNumerosPares(lista_de_numeros: list):
    lista_de_pares = []
    for numero in lista_de_numeros:
        if numero % 2 == 0:
            lista_de_pares.append(numero)
            
    return lista_de_pares

# Punto 9
def calcularProducto(lista_de_numeros: list):
    bandera = True
    for numero in lista_de_numeros:
        if bandera:
            producto = numero
            bandera = False
        else:
            producto *= numero
      
    return producto

# Punto 10
def cadenaPalindromo(cadena: str):

    if cadena == cadena[::-1]:
        print("La cadena es Palindromo")
    else:
        print("La cadena no es Palindromo")


    