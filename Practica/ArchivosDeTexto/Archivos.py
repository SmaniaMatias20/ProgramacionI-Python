import os                                           # Nos permite mediante un metodo saber si existe el archivo
import re

# Escritura
# archivo = open("hola.txt", "w")
# archivo = open("C:\\Users\\Smania Matias\\Desktop\\UTN\\PROG-LAB I\\Practica\\ArchivosDeTexto\\nombre.txt", "w")

# archivo.write("Hola 1BD")                       # Escribir en el archivo, si no existe lo crea.
# archivo.close()                                 # Cierra el archivo y libera la informacion de memoria.

# Lectura
# if os.path.exists("hola.txt"):                  # Preguntar si el archivo existe
#     archivo = open("hola.txt", "r")             # Abrir el archivo
#     informacion = archivo.read(3)               # Manipulo el archivo (escribir/leer) [(3) cantidad de caracteres que quiero que lea].

#     print(informacion)
#     # Hola 1BD

#     archivo.close()                             # Cierra el archivo y libera la informacion de memoria.
# else:
#     print("error")


# Propiedades 
# archivo.closed                                  # Para verificar si el archivo se cerro. (True/False)
# archivo.mode                                    # Retorna el modo de acceso con el que se abrio el archivo.
# archivo.name                                    # Retorna el nombre del archivo

# archivo = open("hola.txt", "r")                 # Abrir el archivo

# if os.path.exists("hola.txt"):                  # Preguntar si el archivo existe
#     for linea in archivo.readlines():           # readlines() crea una lista de cada linea.
#         print(linea, end="")                    # end ---> como quiero que termine el print.

#     archivo.close()
# else:
#     print("error")


# archivo = open("hola.txt", "r")                 # Abrir el archivo
                       
# print(archivo.tell())                           # Indica en que byte esta el puntero.   

# if os.path.exists("hola.txt"):                  # Preguntar si el archivo existe
#     for linea in archivo:                       # Solamente recorre el archivo, no guarda una lista en memoria.
#         print(linea, end="")                    # end ---> como quiero que termine el print.
       
#     archivo.close()
# else:
#     print("error")

# Escribo una lista 
# lineas_texto = ["Juan\n", "Juan\n", "Juan\n"]

# archivo = open("archivo.txt", "w")                 # Abrir el archivo.
# archivo.writelines(lineas_texto)                   # Escribo las lineas creadas.
# archivo.close()

# archivo = open("hola.txt", "r")
# archivo.seek(1)                                    # Para mover el puntero (1) al byte 1.
# primer_linea = archivo.readline()
# print(primer_linea)

# WITH ---> Permite abrir y cerrar los archivos.
# if os.path.exists("hola.txt"):  
#     # Abre el archivo
#     with open("hola.txt", "r") as archivo:
#         # Manipulacion
#         for linea in archivo:
#             print(linea, end="")
#         # Estoy en el with    
#         print(archivo.closed)                   # Para verificar si cerro el archivo (False).
#     # Salgo del with    
#     print(archivo.closed)                       # Para verificar si cerro el archivo (True).
# else:
#     print("Error")


# APPEND ---> Para añadir informacion.
# with open("nombre.txt", "a") as archivo:
#     archivo.write("Hola a todos")                 # Se situa en el ultimo byte y vuelve a escribir la informacion nueva.

#----------------------------------------------------------------------------------------------------------------------------
# Segunda clase ARCHIVOS (CSV)

nombres = ["José","Carlos","Ana"]
apellidos = ["Gomez","Ruiz","Pérez"]
edades = [20,19,34]

# Llevar los datos al archivo.

with open("agenda.csv", "w", encoding="UTF8") as archivo:
    for i in range(len(nombres)):
        mensaje = f"{nombres[i]},{apellidos[i]},{edades[i]}\n"
        archivo.write(mensaje)

# Leer los datos del archivo.

# with open("agenda.csv", "r") as archivo:
#     for linea in archivo:
#         print(linea, end = "")

# Manipular los datos

def parsear_agenda(path: str): 
    agenda = []
    with open(path, "r", encoding="UTF8") as archivo:
        for linea in archivo:
            # registro = linea.split(",")
            # print(f"{registro[0]}-{registro[1]}-{registro[2]}", end= "")
            #-------------------------------------------------------------
            registro = re.split(",|\n", linea)
            contacto = {}
            contacto["nombre"] = registro[0]
            contacto["apellido"] = registro[1]
            contacto["edad"] = registro[2]
            agenda.append(contacto)
            
    return agenda

agenda = parsear_agenda("agenda.csv")

if len(agenda) != 0:
    for contacto in agenda:
        print(f"{contacto['nombre']:20}{contacto['apellido']:20}{contacto['edad']:20}")
else:
    print("error")







