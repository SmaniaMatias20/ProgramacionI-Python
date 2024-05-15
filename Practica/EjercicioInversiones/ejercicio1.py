# Ejercicio 01
# Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar
# en la bolsa de valores:
# A) Para ello se cargarán los siguientes datos hasta que el usuario lo decida:
# * Nombre
# * Monto en pesos de la operación (no menor a $10000)
# * Cantidad de instrumentos
# * Tipo (CEDEAR, BONOS, MEP)
# B) Luego del ingreso mostrar en pantalla todos los datos.
# C) Realizar los siguientes informes:
# 1. Tipo de instrumento que más se operó.
# 2. Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron
# más de $50000.
# 3. Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP,
# que menos dinero invirtió. Puede ser más de uno.
# 4. Nombre de los usuarios que invirtieron en CEDEAR, cuya inversión supere el
# monto promedio
# 5. Porcentaje de usuarios que no invirtieron en MEP, siempre y cuando el monto
# no supere los $50000.

lista_de_nombres = ["juan", "pedro", "adrian", "matias", "diego"]
lista_de_pesos = [70000, 60000, 20000, 30000, 40000]
lista_de_cantidad_instrumentos = [151, 192, 100, 250 , 172]
lista_tipo_de_instrumento = ["CEDEAR", "BONOS", "MEP", "CEDEAR", "BONOS"]

# Punto A

while True:

    nombre = input("Ingrese su nombre: ")

    while not nombre.isalpha() or nombre == None:
        nombre = input("Ingrese su nombre correctamente: ")

    lista_de_nombres.append(nombre)

    monto_operacion = input("Ingrese el monto de la operacion: ")

    while not monto_operacion.isdigit() or monto_operacion == None or int(monto_operacion) < 10000:
        monto_operacion = input("Ingrese el monto de la operacion correctamente: ") 
    
    lista_de_pesos.append(monto_operacion)

    cantidad_instrumento = input("Ingrese la cantidad de instrumentos: ") 

    while not cantidad_instrumento.isdigit() or cantidad_instrumento == None:
        cantidad_instrumento = input("Ingrese la cantidad de instrumentos correctamente: ") 

    lista_de_cantidad_instrumentos.append(cantidad_instrumento)

    tipo_instrumento = input("Ingrese el tipo de instrumento: ")
    tipo_instrumento = tipo_instrumento.upper()

    while tipo_instrumento != "CEDEAR" and tipo_instrumento != "BONOS" and tipo_instrumento != "MEP":
        tipo_instrumento = input("Ingrese el tipo de instrumento correctamente: ")
        tipo_instrumento = tipo_instrumento.upper()
    
    lista_tipo_de_instrumento.append(tipo_instrumento)
    
    continuar = input("¿Desea continuar? SI/NO: ")
    continuar = continuar.upper()

    if continuar != "SI":
        break

# Punto B
for i, nombre in enumerate(lista_de_nombres):
    print(
    f"""
    Nombre: {nombre} 
    Pesos: {lista_de_pesos[i]}
    Cantidad: {lista_de_cantidad_instrumentos[i]}
    Tipo: {lista_tipo_de_instrumento[i]}
    \n
    """)  


# Punto 1
contador_cedear = 0
contador_mep = 0
contador_bonos = 0
for instrumento in lista_tipo_de_instrumento:
    if instrumento == "CEDEAR":
        contador_cedear += 1
    elif instrumento == "MEP":
        contador_mep += 1
    else:
        contador_bonos += 1 


if contador_cedear > contador_bonos and contador_cedear > contador_mep:
    print("El tipo de instrumento que mas se opero es: CEDEAR")
elif contador_bonos > contador_cedear and contador_bonos > contador_mep:
    print("El tipo de instrumento que mas se opero es: BONOS")
else:
    print("El tipo de instrumento que mas se opero es: MEP")

# Punto 2
contador_usuarios = 0
for i, tipo in enumerate(lista_tipo_de_instrumento):
    if tipo == "BONOS":
        if lista_de_cantidad_instrumentos[i] >= 150 and lista_de_cantidad_instrumentos[i] <= 200:
            if lista_de_pesos[i] > 50000:
                contador_usuarios += 1

print(f"La cantidad de usuarios que compraron entre 150 y 200 bonos y que invirtieron mas de $50000 es: {contador_usuarios}")

# Punto 3
bandera = True
indice = 0
for i, tipo in enumerate(lista_tipo_de_instrumento):

    if tipo == "BONOS" or tipo == "MEP":

        if bandera:
            inversion_minima = lista_de_pesos[i]
            bandera = False
            indice = i
            
        if lista_de_pesos[i] < inversion_minima:
            inversion_minima = lista_de_pesos[i] 
            indice = i
                       
print(f"\n{lista_de_nombres[indice]}, fue el que menos dinero invirtio (${inversion_minima}). Compro {lista_de_cantidad_instrumentos[indice]} instrumentos")

# Punto 4
acumulador = 0
usuarios_que_superan_el_promedio = []
for inversion in lista_de_pesos:
    acumulador += inversion

promedio = acumulador / lista_de_pesos.__len__()

for i, tipo in enumerate(lista_tipo_de_instrumento):
    
    if tipo == "CEDEAR" and lista_de_pesos[i] > promedio:
        usuarios_que_superan_el_promedio.append(lista_de_nombres[i]) 

print("Los usuarios que invirtieron en CEDEAR y su inversion superan el monto promedio son...")
for nombre in usuarios_que_superan_el_promedio:
    print(nombre)

# Punto 5

contador = 0
for i, tipo in enumerate(lista_tipo_de_instrumento):
    if tipo != "MEP" and lista_de_pesos[i] < 50000:
        contador += 1

porcentaje = contador * 100 / lista_de_nombres.__len__()

print(f"El porcentaje de usuarios que no invirtieron en MEP y su inversion no supera los $5000 es: {porcentaje}%")



