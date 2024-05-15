import re

# REGEX

# [] Conjunto de caracteres "[a-z]"

# \ Permite determinar secuencias especiales y

# escapar caracteres

# "\d"

# . Hace referencia a cualquier caracter "ho.a"

# ^ Empieza con "^hola"

# $ Termina con "mundo$"

# * Ninguna o más ocurrencias "ho.*a"

# + Una o más ocurrencias "ho.+a"

# ? Cero o una ocurrencia "ho.?a"

# {} Especifica el número de ocurrencias "ho.{1}a"

# | Una o la otra "hola|chau"

# () Permite seleccionar un grupo


#-------------FINDALL------------------
# Busca coincidencias.

texto = "Uno 1 Dos 239 Tres 3 Cuatro 44"
print(re.findall(" ", texto))
# [' ', ' ', ' ', ' ', ' ', ' ', ' ']
print(re.findall("[0-9]+", texto))        # [0-9]+ Numeros del 0-9 mas de uno.
# ['1', '239', '3', '44']
print(re.findall("[a-zA-Z]{3,6}", texto))   # [a-zA-z]{3,6} Letras de la A a la Z (minusculas y mayusculas) como minimo 3 y como maximo 6 caracteres.
# ['Uno', 'Dos', 'Tres', 'Cuatro']


#----------------SUB---------------------
# Reemplaza una cosa con otra.

texto_b = "abc abc ccc ddd abc aaa     256"


result = re.sub("abc", "xyz", texto_b)         # re.sub(patron a reemplazar, nueva cadena, texto donde lo voy a buscar).
print(result)
# xyz xyz ccc ddd xyz aaa     256

result = re.sub(r"\s+", " ", texto_b)             # Reemplaza los espacios en la cadena de texto. (en este caso por nada).                                                
print(result)                                     # "\s" (espacio) r"\s+" (mas de un espacio) "\s\s" (dos espacios).
# abc abc ccc ddd abc aaa 256

print(r"hola \t como \n estan")                   # r para indicar que es una expresion regular.  
# hola \t como \n estan

print("hola \t como \n estan")                    
# hola     como
# estan

#----------------SPLIT------------------
# Separa a traves de un patron. 

print(re.split(" ", "Hola mundo"))              # re.split(patron por el que va a separar, cadena).
# ['Hola', 'mundo']

print(re.split("[a-z]", "hola mundo 125c"))            # No va a contemplar los caracteres de la [a-z].
# ['', '', '', '', ' ', '', '', '', '', ' 125', '']    # [a-z] (una ocurrencia) / [a-z]+ (una ocurrencia o mas).

print(re.split("[0-9 ]", "hola mundo 125c")) 
# ['hola', 'mundo', '', '', '', 'c']

print(re.split("hola|chau| ", "hola mundo chau")) 
# ['', '', 'mundo', '', '']

print(re.split("[a-z]|[0-9]| ", "hola mundo @ 12669 chau"))  # No va a contemplar letras de la [a-z], numeros del [0-9] ni espacios. 
# ['', '', '', '', '', '', '', '', '', '', '', '@', '', '', '', '', '', '', '', '', '', '', '']

#----------------------SEARCH------------------
# Si la cadena cumple con un patron. Devuelve un None o un objeto de tipo match.

print(re.search(" ", "Hola"))
# None (Porque no encontro ninguna coincidencia)

print(re.search(" ", "Hola como estan?"))                # span (posicion donde hizo match) / match (con que hizo match).
# <re.Match object; span=(4, 5), match=' '>

print(re.search("como", "Hola como estan?")) 
# <re.Match object; span=(5, 9), match='como'>

print(re.search("como", "Hola como estan?").span())      # Obtener solamente el span.
# (5, 9)

print(re.search("como", "Hola como estan?").start())     # Donde empieza la coincidencia.
# 5

print(re.search("como", "Hola como estan?").end())       # Donde termina la coincidencia.
# 9

print(re.search("[0-9]", "texto con numeros: 123 y letras: aaa"))
# <re.Match object; span=(19, 20), match='1'>

print(re.search("[0-9]+", "texto con numeros: 123 y letras: aaa"))
# <re.Match object; span=(19, 22), match='123'>

print(re.search("[0-9]+", "texto con numeros: 123 y letras: aaa").group())   # Devuelve con que hizo match.
# 123




