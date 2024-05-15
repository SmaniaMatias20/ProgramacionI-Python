# Burbujeo

# Tomar un elemento y compararlo con el resto preguntando si un valor es mayor/menor al otro. Si se cumple se enrocan los valores.

lista = [5,7,3,6,5,4,2,1,3,6,9,8]
lista_2 = ["Luis", "Ana", "Pedro", "Maria", "Belen"] 

# Ordena de menor a mayor.
for i in range(len(lista)-1):
    for j in range(i+1, len(lista)):                # range(DE, HASTA) ---Si i vale 0, j vale 1---
        if lista[i] > lista[j]:
            auxiliar = lista[i]                     # Swap (Intercambio)
            lista[i] = lista[j]
            lista[j] = auxiliar
            #lista[i], lista[j] = lista[j], lista[i]
print(lista)


# Ordena alfabeticamente.
for i in range(len(lista_2)-1):
    for j in range(i+1, len(lista_2)):                
        if lista_2[i] > lista_2[j]:
            auxiliar = lista_2[i]                     
            lista_2[i] = lista_2[j]
            lista_2[j] = auxiliar
print(lista_2)


lista_3 = [{"nombre":"Luis", "edad": 25},{"nombre":"Ana", "edad": 45},{"nombre":"Pedro", "edad": 20},{"nombre":"Maria", "edad": 50},{"nombre":"Belen", "edad": 20}] 

# Ordena primero por edad y despues alfabeticamente.
for i in range(len(lista_3)-1):
    for j in range(i+1, len(lista_3)):                
        if lista_3[i]["edad"] > lista_3[j]["edad"]:
            auxiliar = lista_3[i]                     
            lista_3[i] = lista_3[j]
            lista_3[j] = auxiliar
        elif lista_3[i]["edad"] == lista_3[j]["edad"]:
            if lista_3[i]["nombre"] > lista_3[j]["nombre"]:
                auxiliar = lista_3[i]                     
                lista_3[i] = lista_3[j]
                lista_3[j] = auxiliar
                


for i in range(len(lista_3)):            
    print(f"{lista_3[i]['nombre']}-{lista_3[i]['edad']}")