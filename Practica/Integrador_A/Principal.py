from Data_stark import lista_personajes


# Nombre: Smania Matias
# Comision: 1D


while True:
    # Menu
    print("""-----------------------Menu de opciones------------------------ \n 
    A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe. \n
    B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
    fuerza (MÁXIMO). \n
    C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
    (MÍNIMO). \n 
    D. Recorrer la lista y determinar el peso promedio de los superhéroes
    masculinos (PROMEDIO). \n
    E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
    género) los cuales su fuerza supere a la fuerza promedio de todas las
    superhéroes de género femenino. \n  
    F. Salir. \n""")

    print("---Ingrese una opcion A/B/C/D/E/F---")
    opcion = input()
    opcion = opcion.upper()

    while opcion != "A" and opcion != "B" and opcion != "C" and opcion != "D" and opcion != "E" and opcion != "F":
        print("Error! Ingrese la opcion nuevamente A/B/C/D/E/F")
        opcion = input()
        opcion = opcion.upper()


    match opcion:
        case "A":
            # Punto A
            print("---Lista de Superheroes--- \n")
            for personaje in lista_personajes:
                for clave in personaje:
                    print(f"{clave}: {personaje[clave]}")
                print("\n")   
        case "B":
            # Punto B
            fuerza_maxima = 0
            for i, personaje in enumerate(lista_personajes):
                fuerza = personaje["fuerza"]
                fuerza = int(fuerza)
                if fuerza > fuerza_maxima:
                    fuerza_maxima = fuerza
                    indice = i

            personaje = lista_personajes[indice] 

            print(
                "\n---El Superheroe mas fuerte---"
                "\nIdentidad: ", personaje["identidad"],
                "\nPeso: ", personaje["peso"],
                "\nFuerza: ", personaje["fuerza"]
                )
        case "C":
            # Punto C
            bandera = True
            for i, personaje in enumerate(lista_personajes):
                altura = personaje["altura"]
                altura = float(altura)
                if bandera:
                    altura_minima = altura
                    indice = i
                    bandera = False

                if altura < altura_minima:
                    altura_minima = altura
                    indice = i

            personaje = lista_personajes[indice]

            print(
                "\n---El Superheroe mas bajo---"
                "\nNombre: ", personaje["nombre"],
                "\nIdentidad: ", personaje["identidad"],
                "\nAltura: ", personaje["altura"]
                )
        case "D":
            # Punto D
            acumulador = 0
            contador = 0
            for i, personaje in enumerate(lista_personajes):
                genero = personaje["genero"]
                if genero == "M":
                    peso = float(personaje["peso"])
                    acumulador += peso
                    contador += 1

            promedio = acumulador / contador
            promedio = round(promedio)
            print(f"El promedio de peso de los Superheroes masculinos es: {promedio}")      
        case "E":
            # Punto E
            acumulador = 0
            contador = 0
            for i, personaje in enumerate(lista_personajes):
                genero = personaje["genero"]
                if genero == "F":
                    fuerza = int(personaje["fuerza"])
                    acumulador += fuerza
                    contador += 1
            
            promedio = acumulador / contador
            promedio = round(promedio)

            for i, personaje in enumerate(lista_personajes):
                fuerza = personaje["fuerza"]
                fuerza = int(fuerza)   
                if fuerza > promedio:
                    print(
                        "Nombre: ", personaje["nombre"],
                        "\nPeso: ", personaje["peso"],
                        "\nFuerza: ", personaje["fuerza"] 
                        )       
                print("\n")
        case "F":
            break















