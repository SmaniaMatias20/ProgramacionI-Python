#Inicializacion 
# Los String son inmutables

# Inmutabilidad

# mi_cadena = "hola"
# print(id(mi_cadena))
# mi_cadena = "cadena"
# print(id(mi_cadena))

#--------------------------------------------------------------------------------------------------
# strip(): Elimina los espacios de una cadena. lstrip() o rstrip() para elegir cual espacio borrar (izquierda o derecha).

# mi_cadena = "            esto es una cadena          "

# sin_espacios = mi_cadena.strip()
# print(sin_espacios)

#--------------------------------------------------------------------------------------------------
# upper(): Convierte la cadena a mayusculas.

# mi_cadena = "esto es una cadena"

# mayuscula = mi_cadena.upper()
# print(mayuscula)

#--------------------------------------------------------------------------------------------------
# lower(): Convierte la cadena a minusculas.

# mi_cadena = "ESTO ES UNA CADENA"

# minuscula = mi_cadena.lower()
# print(minuscula)

#--------------------------------------------------------------------------------------------------
# capitalize(): Convierte la primera letra en mayuscula.

# mi_cadena = "esto es una cadena"

# capital = mi_cadena.capitalize()
# print(capital)

#--------------------------------------------------------------------------------------------------
# title(): Convierte la primera letra de cada palabra en mayuscula.

# mi_cadena = "esto es una cadena"

# titulo = mi_cadena.title()
# print(titulo)

#--------------------------------------------------------------------------------------------------
# replace(): Reemplaza fragmentos de la cadena original. Dos parametros, el primero el fragmento a reemplazar y el segundo el fragmento nuevo.

# mi_cadena = "esto es una cadena"

# mi_cadena = mi_cadena.replace("cadena","****")
# print(mi_cadena)

#--------------------------------------------------------------------------------------------------
# split(): Corta la cadena. Devuelve una lista de strings.

# mi_cadena = "Mario,Matias,German,Fausto"

# lista_split = mi_cadena.split(",", 2) # Caracter delimitador ",". Segundo parametro la cantidad de cortes.

# print(lista_split)

#--------------------------------------------------------------------------------------------------
# join(): Se utiliza para unir cadenas. Lo contrario a split() 

# dia = "20"
# mes = "10"
# año = "1987"
# separador = "/"

# fecha = separador.join([dia, mes, año])
# print(fecha)

#--------------------------------------------------------------------------------------------------
# zfill(): Completa una cadena con 0 (ceros) a la izquierda.

# legajo = "555"
# legajo = legajo.zfill(6)

# print(legajo)

#--------------------------------------------------------------------------------------------------
# isalpha() / isdigit() / isalnum().

# mi_cadena = "holadivBD"

# print(mi_cadena.isalpha()) # Devuelve True si en la cadena hay solo letras del abcedario.

# mi_cadena = "1234"

# print(mi_cadena.isdigit()) # Devuelve True si en la cadena hay solo numeros.

#--------------------------------------------------------------------------------------------------
# len(): Para saber el largo de una cadena.

# mi_cadena = "123pepe"

# print(len(mi_cadena))

#--------------------------------------------------------------------------------------------------
# count(): Devuelve la cantidad de insidencias de la subcadena que le pasamos por parametro.

# mi_cadena = "123pepe"

# print(mi_cadena.count("pe")) # 2 (pe pe) 

#--------------------------------------------------------------------------------------------------
# find(): Devuelve la primer insidencia de la subcadena que le pasemos por parametro.

# mi_cadena = "hola hola hola chau hola"

# print(mi_cadena.find("hola"))
# print(mi_cadena.find("hola", 6)) # Comienza a buscar despues de la posicion que le pasemos por parametro.

#--------------------------------------------------------------------------------------------------
# slice  

# mi_cadena = "hola mundo"

# print(mi_cadena[5:10])
# print(mi_cadena[5:])
# print(mi_cadena[::-1])

#--------------------------------------------------------------------------------------------------






