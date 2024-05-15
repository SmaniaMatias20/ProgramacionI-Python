# lista = [5, 6]
# try:
#     a = int(input("Ingrese el dividendo: "))
#     b = int(input("Ingrese el divisor: "))

#     c = a / b 
#     print(c)  

#     print(lista[5])    
# except ZeroDivisionError:
#     print("Error, no se puede dividir por cero")
# except ValueError:
#     print("Error, no ingresaste un numero")
# except NameError:
#     print("Error, variable no inicializada")
# except IndexError:
#     print("Error, el indice de la lista esta fuera de rango")
# except Exception as ex:
#     print(f"Notificar a sistemas el siguiente error: {type(ex)}")


# NO RECOMENDABLE EN LA PRACTICA PERO ES PROPIO DE PYTHON. BLOQUE ELSE.
# try:
#     a = int(input("Ingrese el dividendo: "))
#     b = int(input("Ingrese el divisor: "))
#     c = a / b  
# except ZeroDivisionError:
#     print("Error, no se puede dividir por cero")
# else:    # Si no se capturo ninguna excepcion se ejecuta el else
#     print(c) 


# BLOQUE FINALLY. SE EJECUTA SI O SI. SE UTILIZA PARA LIBERAR RECURSOS, CUANDO TRABAJAMOS CON ARCHIVOS.
# try:
#     a = int(input("Ingrese el dividendo: "))
#     b = int(input("Ingrese el divisor: "))
#     c = a / b  
#     print(c) 
# except ZeroDivisionError:
#     print("Error, no se puede dividir por cero")
# finally:
#     print("Finalizo el programa")


# while True:
#     try:
#         a = int(input("Ingrese un numero: "))  
#         break
#     except ValueError:
#         print("Error, reingrese")

# c = a + 5
# print(c)


#LANZAR VOLUNTARIAMENTE UNA EXCEPCION. (RAISE == THROW EN JAVA)

def pedir_entero(mensaje, mensaje_error, intentos, min, max):
    retorno = None

    for i in range(intentos):
        valor = input(mensaje)
        try:
            valor = int(valor)

            if valor < min or valor > max:
                raise Exception(f"El {valor} esta fuera de rango")
            
            retorno = valor
            break
        except ValueError:
            print(mensaje_error)

    return retorno

try:
    numero = pedir_entero("Ingrese nota: ", "Error al ingresar una nota", 3, 1, 10)
    if numero != None:
        print(f"El numero ingresado es {numero}")
    else:
        print("Maximo de intentos")
except Exception as ex:
    print(ex) 
















