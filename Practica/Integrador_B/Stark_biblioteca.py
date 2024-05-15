from Data_stark import *

# Punto 1.0
def stark_normalizar_datos(lista_personajes: list):
    """
    Brief: 
        Recorre la lista y convierte al tipo de dato correcto las keys.
    Parametros:
        - lista_personajes (list): Se utiliza para poder acceder a todos los personajes.
    Retorno:
        - Un mensaje indicando si se normalizaron los datos o no.
    """
    modificacion = False
    for personaje in lista_personajes:
        for clave in personaje:
            
            if clave == "fuerza" and type(personaje[clave]) != int:
                personaje[clave] = int(personaje[clave])
                modificacion = True            
            elif type(personaje[clave]) != float and (clave == "peso" or clave == "altura"):
                personaje[clave] = float(personaje[clave])
                modificacion = True   

    if modificacion:
        print("Datos normalizados")
    else: 
        print("Hubo un error al normalizar los datos. Verifique que la lista no este vacia o que los datos ya no se hayan normalizado anteriormente.")

# Punto 1.1
def obtener_dato(personaje: dict, clave_ingresada: str):
    """
    Brief: 
        Recorre el diccionario y busca un dato
    Parametros:
        - personaje (dict): Se utiliza para poder acceder a los datos del personaje.
        - clave_ingresada (str): El dato que queremos buscar.
    Retorno:
        - Una cadena con el dato del personaje
        - False si no se encontro el dato.
    """
    validacion = False

    if len(personaje) != 0:
        for clave in personaje:
            if clave == clave_ingresada:
                validacion = True

    dato = personaje[clave_ingresada]

    if validacion:
        return dato
    else:
        return False

# Punto 1.2    
def obtener_nombre(personaje: dict):
    """
    Brief: 
        Obtiene el nombre del personaje.
    Parametros:
        - personaje (dict): Se utiliza para poder acceder a los datos del personaje.
    Retorno:
        - Una cadena con el nombre del personaje.
        - False si no se encontro el nombre.
    """
    dato = obtener_dato(personaje, "nombre")

    if dato != False:
        return dato
    else:
        return False

# Punto 2.0
def obtener_nombre_y_dato(personaje: dict, clave: str):
    """
    Brief: 
        Obtiene el nombre y un dato sobre el personaje.
    Parametros:
        - personaje (dict): Se utiliza para poder acceder a los datos del personaje.
        - clave (str): El dato que queremos obtener. 
    Retorno:
        - Una cadena con el nombre y el dato obtenido del personaje.
        - False si no se encontro el dato.
    """
    nombre = obtener_nombre(personaje)
    dato = obtener_dato(personaje, clave)

    cadena = f"{nombre} | {dato}" 

    if dato != False:
        return cadena
    else:
        return False

# Punto 3.1
def obtener_maximo(lista_personajes: list, clave: str):
    """
    Brief: 
        Obtiene el valor maximo de la clave pasada por parametro.
    Parametros:
        - lista_personajes (list): Se utiliza para poder acceder a los personajes.
        - clave (str): Es el dato que queremos obtener su valor maximo. 
    Retorno:
        - El maximo.
        - False si la lista esta vacia.
    """
    validacion = False
    maximo = 0
    if len(lista_personajes) != 0:
        for personaje in lista_personajes:
            if type(personaje[clave]) == int or type(personaje[clave]) == float:
                if personaje[clave] >= maximo:
                    maximo = personaje[clave]
                    validacion = True
            
    if validacion:
        return maximo
    else:
        return validacion

# Punto 3.2
def obtener_minimo(lista_personajes: list, clave: str):
    """
    Brief: 
        Obtiene el valor minimo de la clave pasada por parametro.
    Parametros:
        - lista_personajes (list): Se utiliza para poder acceder a los personajes.
        - clave (str): Es el dato que queremos obtener su valor minimo. 
    Retorno:
        - El minimo.
        - False si la lista esta vacia.
    """
    validacion = False
    minimo = None
    if len(lista_personajes) != 0:
        for personaje in lista_personajes:
            if type(personaje[clave]) == int or type(personaje[clave]) == float:
                if minimo == None or personaje[clave] <= minimo:
                    minimo = personaje[clave]
                    validacion = True
            
    if validacion:
        return minimo
    else:
        return validacion
    
# Punto 3.3
def obtener_dato_cantidad(lista_personajes: list, valor: int, clave: str):
    """
    Brief: 
        Obtiene un dato que cumpla con cierta condicion.
    Parametros:
        - lista_personajes (list): Se utiliza para poder acceder a todos los personajes.
        - valor (int): La condicion que debe cumplir el dato.
        - clave (str): Tipo de dato que queremos obtener 
    Retorno:
        - Una lista con los nombres que hayan cumplido la condicion.
        - False si la lista esta vacia.
    """
    validacion = False
    lista = []
    if len(lista_personajes) != 0: 
        for personaje in lista_personajes:
            if personaje[clave] == valor:
                lista.append(personaje)
                validacion = True
    
    if validacion:
        return lista
    else:
        return validacion
    

# Punto 3.4
def stark_imprimir_personajes(lista_personajes: list):
    """
    Brief: 
        Imprime la lista de personajes.
    Parametros:
        - lista_personajes (list): Se utiliza para poderla recorrer e imprimir.
    Retorno:
        -No retorna nada.
    """
    if len(lista_personajes) != 0:
        for personaje in lista_personajes:
            for clave in personaje:
                print(f"{clave}: {personaje[clave]}")
            print("\n")  
    else:
        print("False")          
    
# Punto 4.1
def sumar_dato_heroe(lista_personajes: list, clave: str):
    """
    Brief: 
        Suma todos los datos que coincidan con la clave que le pasemos por parametro.
    Parametros:
        - lista_personajes (list): Se utiliza para poder acceder a los personajes.
        - clave (str): El dato que vamos a sumar.
    Retorno:
        - La suma total del dato.
        - False si la lista esta vacia.
    """
    validacion = False
    suma = 0
    
    for personaje in lista_personajes:
        if type(personaje) == dict and len(personaje) != 0:
            if type(personaje[clave]) == int or type(personaje[clave]) == float:
                suma += personaje[clave] 
                validacion = True
    
    if validacion:
        return suma
    else:
        return validacion

# Punto 4.2
def dividir(dividendo: float , divisor: float):
    """
    Brief: 
        Realiza una division con los dos valores pasados por parametro.
    Parametros:
        - dividendo (float): El dividendo de la operacion.
        - divisor (float): El divisor de la operacion.
    Retorno:
        - El resultado de la division.
        - False si divisor es igual a 0.
    """
    if divisor != 0:
        resultado = dividendo / divisor
        return resultado
    else:
        return False

# Punto 4.3
def calcular_promedio(lista_personajes: list, clave: str):
    """
    Brief: 
        Calcula el promedio del dato que le pasemos por parametro.
    Parametros:
        - lista_personajes (list): Se utiliza para poder acceder a los personajes.
        - clave (str): El dato que vamos a calcular su promedio.
    Retorno:
        - El promedio del dato.
        - False si divisor es igual a 0.
    """
    dividendo = sumar_dato_heroe(lista_personajes, clave)
    promedio = dividir(dividendo, len(lista_personajes))
    
    return promedio

# Punto 4.4
def mostrar_promedio_dato(lista_personajes: list, clave: str):
    """
    Brief: 
        Muestra el promedio del dato que le pasemos por parametro.
    Parametros:
        - lista_personajes (list): Se utiliza para poder acceder a los personajes.
        - clave (str): El dato que vamos a calcular su promedio.
    Retorno:
        - El promedio del dato.
        - False si la lista esta vacia.
    """
    validacion = False
    if len(lista_personajes) != 0:
        for personaje in lista_personajes:
            if type(personaje[clave]) == int or type(personaje[clave]) == float:
                promedio = calcular_promedio(lista_personajes, clave)
                validacion = True
                
    if validacion:
        return promedio
    else:
        return validacion
    
# Para los puntos C,D,E,F
def obtener_personajes_por_genero(lista_personajes: list, genero: str):
    """
    Brief: 
        Recorre la lista y obtiene una lista con el genero solicitado por parametro.
    Parametros:
        - lista_personajes (list): Se utiliza para poder acceder a todos los personajes.
        - genero (str): Tipo de datos que queremos obtener.
    Retorno:
        - Una lista con todos los personajes del genero solicitado.
        - False si la lista esta vacia.
    """
    lista_personajes_genero = []
    validacion = False
    if len(lista_personajes) != 0 and (genero == "NB" or genero == "M" or genero == "F"):
        validacion = True
        for personaje in lista_personajes:
            if personaje["genero"] == genero:
                lista_personajes_genero.append(personaje)

    if validacion:
        return lista_personajes_genero
    else:
        return False
    
# Punto 5.1
def imprimir_menu(menu: str):
    """
    Brief: 
        Imprime por consola el dato pasado por parametro.
    Parametros:
        - menu (str): El dato que queremos imprimir por consola.
    Retorno:
        - El menu con opciones.
    """
    print(menu)
    
# Punto 5.2
def validar_entero(opcion: str):
    """
    Brief: 
        Valida si el parametro ingresado es un string que contenga solo numeros.
    Parametros:
        - opcion (str): El dato que vamos a validar.
    Retorno:
        - True si el string contiene solo numeros.
        - False en caso contrario.
    """
    if opcion.isdigit():
        return True
    else:
        return False

# Punto 5.3
def stark_menu_principal(menu: str):
    """
    Brief: 
        Imprime el menu de opciones, valida y castea a entero la opcion solicitada.
    Parametros:
        - menu (str): El menu que debe mostrar por consola.
    Retorno:
        - La opcion elegida casteada a entero.
        - False si la opcion no cumple con la validacion.
    """
    imprimir_menu(menu)
    opcion = input("Ingrese la opcion: ")
    validacion = validar_entero(opcion)

    if validacion:
        return int(opcion)
    else:
        return False
    

# Punto 6
def stark_marvel_app(lista_personajes: list, menu: str):
    """
    Brief: 
        Accede a traves de la opcion elegida al menu.
    Parametros:
        - lista_personajes (list): Se utiliza para poder acceder a todos los personajes.
        - menu (str): El menu que se va a mostrar por consola.
    Retorno:
        - No retorna nada.
    """
    while True:

        opcion = stark_menu_principal(menu)

        match opcion:
            case 1:
                stark_normalizar_datos(lista_personajes)
            case 2:
                dato = obtener_dato(lista_personajes[0], "genero")
                print(f"El dato obtenido es: {dato}")
            case 3:
                nombre = obtener_nombre(lista_personajes[5])
                print(f"El nombre del personaje es: {nombre}")
            case 4:
                clave = "identidad"
                nombre_y_dato = obtener_nombre_y_dato(lista_personajes[3], clave)
                print(nombre_y_dato)
            case 5:
                clave = "peso"
                maximo = obtener_maximo(lista_personajes, clave)
                print(f"El maximo de {clave} es: {maximo}")
            case 6:
                clave = "altura"
                minimo = obtener_minimo(lista_personajes, clave)
                print(f"El minimo de {clave} es: {minimo}")
            case 7:
                clave = "fuerza"
                lista_personajes_fuerza = obtener_dato_cantidad(lista_personajes, 15, clave)
                if lista_personajes_fuerza != False:
                    stark_imprimir_personajes(lista_personajes_fuerza)
            case 8:
                stark_imprimir_personajes(lista_personajes)
            case 9:
                clave = "peso"
                suma = sumar_dato_heroe(lista_personajes, clave)
                print(f"El resultado de la suma de todos los {clave} es: {suma}")
            case 10:
                dividendo = 100
                divisor = 50
                resultado = dividir(dividendo, divisor)
                print(f"El resultado de la division es: {resultado}")
            case 11:
                clave = "altura"
                promedio = calcular_promedio(lista_personajes, clave)
                print(f"El promedio de {clave} es: {promedio}")
            case 12:
                clave = "peso"
                promedio = mostrar_promedio_dato(lista_personajes, clave)
                print(f"El promedio de {clave} es: {promedio}")
            case 13:
                genero = "F"
                lista_personajes_por_genero = obtener_personajes_por_genero(lista_personajes, genero)
                stark_imprimir_personajes(lista_personajes_por_genero)
            case 14:
                break
            case _:
                print("Opcion incorrecta")

# Punto 7
def segundo_menu(lista_personajes: list, menu: str):
    """
    Brief: 
        Accede a traves de la opcion elegida al menu.
    Parametros:
        - lista_personajes (list): Se utiliza para poder acceder a todos los personajes.
        - menu (str): El menu que se va a mostrar por consola.
    Retorno:
        - No retorna nada.
    """
    while True:

        opcion = stark_menu_principal(menu)

        match opcion:
            case 1:
                stark_normalizar_datos(lista_personajes)
            case 2:
                # Recorrer la lista imprimiendo por consola el nombre de cada personaje de género NB.
                for personaje in lista_personajes:
                    nombre_y_dato = obtener_nombre_y_dato(personaje, "genero")
                    if personaje["genero"] == "NB":
                        print(nombre_y_dato)
            case 3:
                # Recorrer la lista y determinar cuál es el personaje más alto de género F.
                lista_genero_femenino = obtener_personajes_por_genero(lista_personajes, "F")
                maximo_altura = obtener_maximo(lista_genero_femenino, "altura")
                lista_femenino_maximo_altura = obtener_dato_cantidad(lista_genero_femenino, maximo_altura, "altura")
                print(f"\n---El/los superheroe mas alto de genero femenino es/son---\n")
                stark_imprimir_personajes(lista_femenino_maximo_altura)
            case 4:
                # Recorrer la lista y determinar cuál es el personaje más alto de género M.
                lista_genero_masculino = obtener_personajes_por_genero(lista_personajes, "M")
                maximo_altura = obtener_maximo(lista_genero_masculino, "altura")
                lista_masculino_maximo_altura = obtener_dato_cantidad(lista_genero_masculino, maximo_altura, "altura")
                print(f"\n---El/los personaje mas alto de genero masculino es/son---\n")
                stark_imprimir_personajes(lista_masculino_maximo_altura)
            case 5:
                # Recorrer la lista y determinar cuál es el personaje más débil de género M.
                lista_genero_masculino = obtener_personajes_por_genero(lista_personajes, "M")
                minimo_fuerza = obtener_minimo(lista_genero_masculino, "fuerza")
                lista_masculino_minimo_fuerza = obtener_dato_cantidad(lista_genero_masculino, minimo_fuerza, "fuerza")
                print(f"\n---El/los personaje mas debil de genero masculino es/son---\n")
                stark_imprimir_personajes(lista_masculino_minimo_fuerza)
            case 6:
                # Recorrer la lista y determinar cuál es el personaje más débil de género NB.
                lista_genero_no_binario = obtener_personajes_por_genero(lista_personajes, "NB")
                minimo_fuerza = obtener_minimo(lista_genero_no_binario, "fuerza")
                lista_no_binario_minimo_fuerza = obtener_dato_cantidad(lista_genero_no_binario, minimo_fuerza, "fuerza")
                print(f"\n---El/los personaje mas debil de genero no binario es/son---\n")
                stark_imprimir_personajes(lista_no_binario_minimo_fuerza)
            case 7:
                # Recorrer la lista y determinar la fuerza promedio de los personajes de género NB.
                lista_genero_no_binario = obtener_personajes_por_genero(lista_personajes, "NB")
                promedio = mostrar_promedio_dato(lista_genero_no_binario, "fuerza")
                print(f"El promedio de fuerza de los personajes de genero NB es: {promedio}")
            case 8:
                # Determinar cuántos personajes tienen cada tipo de color de ojos.
                color_ojos = "Brown"
                lista_color_ojos = listar_personajes_por_color_de_ojos(lista_personajes, color_ojos)
                contador = len(lista_color_ojos)
                print(f"La cantidad de personajes con ojos {color_ojos} es: {contador}")
            case 9:
                # Determinar cuántos personajes tienen cada tipo de color de pelo.
                tipo_pelo = "Auburn"
                contador = cantidad_personajes_por_color_de_pelo(lista_personajes, tipo_pelo)
                print(f"La cantidad de personajes con pelo {tipo_pelo} es: {contador}")
            case 10:
                # Listar todos los personajes agrupados por color de ojos.
                color_ojos = "Brown"
                lista_color_ojos = listar_personajes_por_color_de_ojos(lista_personajes, color_ojos)
                print(f"Lista de personajes con color de ojos {color_ojos}---\n")
                stark_imprimir_personajes(lista_color_ojos)
            case 11:
                # Listar todos los personajes agrupados por tipo de inteligencia.
                inteligencia = "good"
                lista_inteligencia = listar_personajes_por_inteligencia(lista_personajes, inteligencia)
                print(f"Lista de personajes con inteligencia {inteligencia}---\n")
                stark_imprimir_personajes(lista_inteligencia)
            case 12:
                break
            case _:
                print("Opcion incorrecta")


def crear_menu():
    """
    Brief: 
        Crea los diferentes menu, los asigna en las variables y los guarda en una lista.
    Parametros:
        - No recibe parametros.
    Retorno:
        - Una lista con los menu. 
    """
    menu_inicio = """
    ------------Menu de inicio------------
    1. Menu funciones.
    2. Menu ejercicios.
    3. Salir.
    """

    menu_ejercicios = """
    ------------Menu de ejercicios (Punto 7)------------
    1. Normalizar datos (No se debe poder acceder a los otros puntos).
    2. Recorrer la lista imprimiendo por consola el nombre de cada personaje de género NB.
    3. Recorrer la lista y determinar cuál es el personaje más alto de género F.
    4. Recorrer la lista y determinar cuál es el personaje más alto de género M.
    5. Recorrer la lista y determinar cuál es el personaje más débil de género M.
    6. Recorrer la lista y determinar cuál es el personaje más débil de género NB.
    7. Recorrer la lista y determinar la fuerza promedio de los personajes de género NB.
    8. Determinar cuántos personajes tienen cada tipo de color de ojos.
    9. Determinar cuántos personajes tienen cada tipo de color de pelo.
    10. Listar todos los personajes agrupados por color de ojos.
    11. Listar todos los personajes agrupados por tipo de inteligencia.
    12. Salir
    """

    menu_funciones = """
    ------------Menu de funciones (Punto 6)------------
    1. Normalizar datos (No se debe poder acceder a los otros puntos).
    2. Obtener dato.
    3. Obtener nombre.
    4. Obtener nombre y dato.
    5. Obtener maximo.
    6. Obtener minimo.
    7. Obtener dato cantidad.
    8. Imprimir personajes.
    9. Sumar datos personajes.
    10. Dividir.
    11. Calcular promedio.
    12. Mostrar promedio.
    13. Obtener superheroes por genero
    14. Salir
    """

    lista_de_menus = [menu_inicio, menu_funciones, menu_ejercicios]

    return lista_de_menus

def listar_personajes_por_inteligencia(lista_personajes: list, tipo_inteligencia: str):
    """
    Brief: 
        Agrupa los personajes por inteligencia.
    Parametros:
        - lista_personajes (list): Se utiliza para poder acceder a todos los personajes.
        - tipo_inteligencia (str): El dato por el cual vamos a agrupar.
    Retorno:
        - Una lista de superheroes que cumpla con la condicion.
    """
    lista_inteligencia = []
    for personaje in lista_personajes:
        inteligencia = obtener_dato(personaje, "inteligencia") 
        if inteligencia == tipo_inteligencia:
            lista_inteligencia.append(personaje)

    return lista_inteligencia


def listar_personajes_por_color_de_ojos(lista_personajes: list, tipo_ojos: str):
    """
    Brief: 
        Agrupa los personajes por color de ojos.
    Parametros:
        - lista_personajes (list): Se utiliza para poder acceder a todos los personajes.
        - tipo_ojos (str): El dato por el cual vamos a agrupar.
    Retorno:
        - Una lista de superheroes que cumpla con la condicion.
    """
    lista_color_ojos = []

    for personaje in lista_personajes:
        color_ojos = obtener_dato(personaje, "color_ojos")
        if color_ojos == tipo_ojos:
            lista_color_ojos.append(personaje)


    return lista_color_ojos

def cantidad_personajes_por_color_de_pelo(lista_personajes: list, tipo_pelo: str):
    """
    Brief: 
        Cuenta los personajes segun su tipo de pelo.
    Parametros:
        - lista_personajes (list): Se utiliza para poder acceder a todos los personajes.
        - tipo_pelo (str): El dato por el cual vamos a agrupar.
    Retorno:
        - La cantidad de personajes que cumpla la condicion.
    """
    contador = 0
    for personaje in lista_personajes:
       pelo = obtener_dato(personaje, "color_pelo") 
       if pelo == tipo_pelo:
           contador += 1

    return contador

