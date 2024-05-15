from Data_stark import *
import re

# Punto 1.1
def extraer_iniciales(nombre_personaje: str):
    """
    Brief: 
        Extrae las iniciales de una cadena.
    Parametros:
        - nombre_personaje str: La cadena de la que se van a extraer las iniciales.
    Retorno:
        - Las iniciales.
        - False.
    """

    if type(nombre_personaje) == str and len(nombre_personaje) != 0:
        if re.search("-", nombre_personaje) != None:
            nombre_personaje = re.sub("-", " ", nombre_personaje) 
        elif re.search("the", nombre_personaje) != None:
            nombre_personaje = re.sub("the", "", nombre_personaje) 

        iniciales = re.sub("[a-z]", " ", nombre_personaje)
        iniciales = re.sub(r"\s+", " ", iniciales) 
        iniciales = iniciales.replace(" ", ".") 
        
        return iniciales
    else:
        return False

# Punto 1.2
def obtener_dato_formato(dato: str):
    """
    Brief: 
        Convierte el dato a minusculas y con formato snake_case.
    Parametros:
        - dato str: un string con un dato especifico.
    Retorno:
        - El dato convertido.
        - False.
    """
    if type(dato) == str and len(dato) != 0:
        dato = re.sub(" ", "_", dato)   
        return dato.lower()
    else:
        return False

# Punto 1.3  
def stark_imprimir_nombre_con_iniciales(nombre_personaje: str):
    """
    Brief: 
        Imprime el parametro con un formato especifico.
    Parametros:
        - nombre_personaje str: una cadena con un dato especifico.
    Retorno:
        - La cadena formateada.
        - False.
    """
    nombre = obtener_dato_formato(nombre_personaje)
    iniciales = extraer_iniciales(nombre_personaje)

    if nombre != False and iniciales != False:
        cadena = "* " + nombre + "(" + iniciales + ")"
        return cadena 
    else:
        return False

# Punto 1.4
def stark_imprimir_nombres_con_iniciales(lista_personajes: list):
    """
    Brief: 
        Imprime la lista con un formato especifico.
    Parametros:
        - lista_personajes list: La lista de personajes. 
    Retorno:
        - True.
        - False.
    """
    if type(lista_personajes) == list and len(lista_personajes) != 0:
        for personaje in lista_personajes:
            cadena = stark_imprimir_nombre_con_iniciales(personaje["nombre"])
            print(cadena)
        return True
    else:
        return False


# Punto 2.1
def generar_codigo_heroe(personaje: dict, id_personaje: int):
    """
    Brief: 
        Genera el codigo de cada personaje.
    Parametros:
        - personaje dict: El personaje 
        - id_personaje int: El ID del personaje  
    Retorno:
        - El codigo.
        - False.
    """
    codigo = ""
    if type(id_personaje) == int and type(personaje) == dict and len(personaje) != 0:
        id_personaje = str(id_personaje)
        genero = personaje["genero"]

        match genero:
            case "F":
                if len(id_personaje) < 7:
                    id_personaje = id_personaje.zfill(7)
                
                separador = "-2"
                codigo = separador.join([genero, id_personaje])
            case "M":
                if len(id_personaje) < 7:
                    id_personaje = id_personaje.zfill(7)
                
                separador = "-1"
                codigo = separador.join([genero, id_personaje])
            case "NB":
                if len(id_personaje) < 6:
                    id_personaje = id_personaje.zfill(6)
         
                separador = "-0"
                codigo = separador.join([genero, id_personaje])
            case _:
                return False  
    else:
        return False
    
    if len(codigo) > 10:
        return False
    else:
        return codigo
    

# Punto 2.2
def stark_generar_codigos_heroes(lista_personajes: list):
    """
    Brief: 
        Itera la lista y genera cada uno de los codigos.
    Parametros:
        - lista_personajes list: Lista de personajes.
    Retorno:
        - Una cadena con el nombre y el codigo.
        - N/A.
    """
    if type(lista_personajes) == list and len(lista_personajes) != 0:
        for i, personaje in enumerate(lista_personajes):
            if type(personaje) == dict and len(personaje) != 0:
                nombre = stark_imprimir_nombre_con_iniciales(personaje["nombre"])
                codigo = generar_codigo_heroe(personaje, i+1)
                print(f"{nombre} | {codigo}")
            else:
                print("N/A")
        print(f"---Se asignaron {i+1} codigos---")
    else:
        print("N/A")
    
# Punto 3.1
def sanitizar_entero(numero_str: str):
    """
    Brief: 
        Verifica si el string ingresado por parametro es un numero entero.
    Parametros:
        - numero_str str: Un string que representa un posible numero entero.
    Retorno:
        - El numero casteado a entero.
        - -2 (si el numero es negativo).
        - -1 (si contiene caracteres no numericos).
        - -3 (si ocurren otros errores).
    """
    if type(numero_str) == str:
        if re.search(" ", numero_str) != None:
            numero_str = re.sub(r"\s+", "", numero_str)
        
        for caracter in numero_str:
            if caracter.isalpha() or not caracter.isalnum() and caracter != "-":
                return -1
            
        if numero_str.count("-") == 0 :    
            numero_str = int(numero_str)
            return numero_str
        elif numero_str.count("-") == 1 and re.search("-", numero_str).start() == 0:
            return -2
        else:
            return -3
    else:
        return -3

# Punto 3.2
def sanitizar_flotante(numero_str: str):
    """
    Brief: 
        Verifica si el string ingresado por parametro es un numero flotante.
    Parametros:
        - numero_str str: Un string que representa un posible numero flotante.
    Retorno:
        - El numero casteado a flotante.
        - -2 (si el numero es negativo).
        - -1 (si contiene caracteres no numericos).
        - -3 (si ocurren otros errores).
    """
    if type(numero_str) == str:
        if re.search(" ", numero_str) != None:
            numero_str = re.sub(r"\s+", "", numero_str)
        
        contador_puntos = 0
        for caracter in numero_str:
            if caracter.isalpha() or not caracter.isalnum() and caracter != "." and caracter != "-":
                return -1
            elif caracter == ".":
                contador_puntos += 1
            
        if contador_puntos <= 1 and numero_str.count("-") == 0:    
            numero_str = float(numero_str)
            return numero_str
        elif numero_str.count("-") == 1 and re.search("-", numero_str).start() == 0:
            return -2
        else:
            return -3
    else:
        return -3
 
# Punto 3.3
def sanitizar_string(valor_str: str, valor_por_defecto: str = "-"):
    """
    Brief: 
        Analiza el string recibido y determina si es solo texto.
    Parametros:
        - valor_str str: El dato a analizar.
        - valor_por_defecto str: Representa un valor por defecto.
    Retorno:
        - N/A
        - valor_str (en minuscula)
        - False
    """

    if type(valor_str) == str:

        valor_str = valor_str.strip()   
        
        if re.search("/", valor_str) != None:
            valor_str = re.sub("/", " ", valor_str) 
        
        for caracter in valor_str:
            if caracter.isdigit():
                return "N/A"
            
        if len(valor_str) != 0:
            return valor_str.lower()  
        else:
            return False
    else:
        return False         

# Punto 3.4
def sanitizar_dato(personaje: dict, clave: str, tipo_de_dato: str):
    """
    Brief: 
        Sanitiza el valor del diccionario correspondiente a la clave y al tipo de dato recibido.
    Parametros:
        - personaje dict: Diccionario con los datos del personaje.
        - clave str: String que representa el dato a sanitizar.
        - tipo_de_dato str: String que representa el tipo de dato a sanitizar. 
    Retorno:
        - True
        - False
    """
    validacion = False
    
    for llave in personaje:
        if clave == llave:
            validacion = True

    tipo_de_dato.lower()
    if validacion:
        if tipo_de_dato == "string":
            dato = sanitizar_string(personaje[clave])        
            return True
        elif tipo_de_dato == "flotante":
            dato = sanitizar_flotante(personaje[clave])     
            return True
        elif tipo_de_dato == "entero":
            dato = sanitizar_entero(personaje[clave])       
            return True
        else:
            print("Tipo de dato no reconocido!")
            return False
    else:
        return False      



# Punto 3.5
def stark_normalizar_datos(lista_personajes: list):
    """
    Brief: 
        Recorre la lista de héroes y sanitiza los valores.
    Parametros:
        - lista_personajes list: Lista de personajes.
    Retorno:
        - No retorna nada.
    """
    if len(lista_personajes) != 0:
        for personaje in lista_personajes:
            for clave in personaje:
                if clave == "color_ojos" or clave == "color_pelo" or clave == "inteligencia": 
                    if len(personaje[clave]) != 0: 
                        dato = sanitizar_dato(personaje, clave, "string")
                    else:
                        dato = re.sub("", "No tiene", personaje[clave]) 
                elif clave == "altura" or clave == "peso":
                    dato = sanitizar_dato(personaje, clave, "flotante")   
                elif clave == "fuerza":
                    dato = sanitizar_dato(personaje, clave, "entero")
    else:
        print("Error, lista de personajes vacia")
                

# Punto 4.1
def stark_imprimir_indice_nombre(lista_personajes: list):
    """
    Brief: 
        Muestra por pantalla cada una de las palabras (en 
        minúscula) de cada uno de los nombres que existan en el data_stark 
        separado por un guión entre cada una de las palabras, ignorando las palabras 
        que contengan “the”.
    Parametros:
        - lista_personajes list: Lista de personajes.
    Retorno:
        - No retorna nada.
    """
    for personaje in lista_personajes:
        for clave in personaje:
            if clave == "nombre":
                if re.search("the", personaje[clave]) != None:
                    personaje[clave] = re.sub(" the ", "-", personaje[clave])  
                
                personaje[clave] = re.sub(" ", "-", personaje[clave]) 

                print(personaje[clave], end = "")
        print("-", end="")


# Punto 5.1
def generar_separador(patron: str, largo: int, imprimir: bool = True):
    """
    Brief: 
        Genera un string que contenga el patrón especificado repitiendo tantas veces como la 
        cantidad recibida como parámetro.
    Parametros:
        - patron str: Carácter que se utilizará como patrón para generar el separador.
        - largo str: Número que representa la cantidad de caracteres que va ocupar el separador.
        - imprimir bool: Parámetro opcional del tipo booleano (por default definido en True).  
    Retorno:
        - El patron.
        - N/A 
    """
    if len(patron) != 0 and largo > 0 and largo < 235:
        if imprimir:
            for i in range(largo):
                print(patron, end="")   
        else:
            return patron
    else:
        return "N/A"
        
# Punto 5.2
def generar_encabezado(titulo: str):
    """
    Brief: 
        Devuelve un string que contenga el título envuelto entre dos separadores.
    Parametros:
        - titulo str: String que representa el título de una sección de la ficha.  
    Retorno:
        - No retorna nada.
    """
    generar_separador("*", 150)
    print(f"\n{titulo.upper()}")
    generar_separador("*", 150)

# Punto 5.3
def imprimir_ficha_heroe(personaje: dict):
    """
    Brief: 
        Genera un string a partir de los datos del heroe con un formato especifico.
    Parametros:
        - personaje dict: Diccionario con los datos del héroe
    Retorno:
        - No retorna nada.
    """
    nombre_con_iniciales = stark_imprimir_nombre_con_iniciales(personaje["nombre"])
    identidad_secreta = obtener_dato_formato(personaje["identidad"])
    consultora = obtener_dato_formato(personaje["empresa"]) 
    codigo = generar_codigo_heroe(personaje, 1)

    generar_encabezado("Principal")
    print(f"""\n
    NOMBRE DEL HEROE:            {nombre_con_iniciales}
    IDENTIDAD SECRETA:           {identidad_secreta}
    CONSULTORA:                  {consultora}
    CODIGO DE PERSONAJE:         {codigo}
    """)
    

    generar_encabezado("Fisico")
    print(f"""\n
    ALTURA:                     {personaje['altura']} cm
    PESO:                       {personaje['peso']} kg
    FUERZA:                     {personaje['fuerza']} N
    """)

    generar_encabezado("Señas Particulares")
    print(f"""\n
    COLOR DE OJOS:              {personaje['color_ojos']}
    COLOR DE PELO:              {personaje['color_pelo']}
    """)

# Punto 5.4
def stark_navegar_fichas(lista_personajes: list):
    indice = 0
    imprimir_ficha_heroe(lista_personajes[indice])

    while True:
        opcion = input("Ingrese la opcion 1/2/3: ")
        match opcion:
            case "1":
                indice = indice - 1
                if indice < 0:
                    indice = len(lista_personajes) - 1
                    imprimir_ficha_heroe(lista_personajes[indice])
                else: 
                    imprimir_ficha_heroe(lista_personajes[indice])
            case "2": 
                indice = indice + 1
                if indice >= len(lista_personajes):
                    indice = 0
                    imprimir_ficha_heroe(lista_personajes[indice])
                else: 
                    imprimir_ficha_heroe(lista_personajes[indice])
            case "3":
                break
            case _:
                break

def imprimir_menu():
    """
    Brief: 
        Imprime el menu
    Parametros:
        - No recibe ningun parametro.
    Retorno:
        - El menu.
    """
    print(
    """ Menu de opciones:   
    1 - Imprimir la lista de nombres junto con sus iniciales.
    2 - Imprimir la lista de nombres y el código del mismo.
    3 - Normalizar datos.
    4 - Imprimir índice de nombres.
    5 - Navegar fichas.
    6 - Salir.
    """)

def stark_menu_principal():
    """
    Brief: 
        Imprime el menu de opciones, valida y castea a entero la opcion solicitada.
    Parametros:
        - No recibe ningun parametro.
    Retorno:
        - La opcion elegida casteada a entero.
        - False si la opcion no cumple con la validacion.
    """
    imprimir_menu()
    opcion = input("Ingrese la opcion: ")
    opcion = sanitizar_entero(opcion)

    if opcion > 0:
        return int(opcion)
    else:
        return False


def stark_marvel_app(lista_personajes: list):
    """
    Brief: 
        Accede a traves de la opcion elegida al menu.
    Parametros:
        - lista_personajes (list): Se utiliza para poder acceder a todos los personajes.
    Retorno:
        - No retorna nada.
    """
    while True:

        opcion = stark_menu_principal()

        match opcion:
            case 1:
                stark_imprimir_nombres_con_iniciales(lista_personajes)
            case 2:
                stark_generar_codigos_heroes(lista_personajes)
            case 3:
                stark_normalizar_datos(lista_personajes)
            case 4:
                stark_imprimir_indice_nombre(lista_personajes)
            case 5:
                stark_navegar_fichas(lista_personajes)
            case 6:
                break
            




