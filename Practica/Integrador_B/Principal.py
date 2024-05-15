from Data_stark import lista_personajes
from Stark_biblioteca import *


# Nombre: Smania Matias
# Comision: 1D


lista_de_menus = crear_menu() 

normalizar = input("¿Desea normalizar los datos para continuar? SI/NO\n")

while normalizar.upper() != "SI":
    normalizar = input("Debe normalizar los datos antes de continuar... SI/NO\n")

stark_normalizar_datos(lista_personajes)

while True:

    opcion = stark_menu_principal(lista_de_menus[0])

    if opcion == 1:
        stark_marvel_app(lista_personajes, lista_de_menus[1])
    elif opcion == 2:
        segundo_menu(lista_personajes, lista_de_menus[2])
    elif opcion == 3:
        break
    else: 
        print("Opcion incorrecta")









