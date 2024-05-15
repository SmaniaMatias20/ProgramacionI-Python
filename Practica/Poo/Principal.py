from Avion import Avion
from Poo import Personaje
from Transporte import Transporte
from Auto import Auto

personaje = Personaje(5, "IronMan", True, 150, True)
# print(personaje.retornar_descripcion())

# otro_personaje = Personaje(6, "Thor", True, 190, False)
# print(otro_personaje.retornar_descripcion())

# personaje.luchar(otro_personaje) # Relacion de colaboracion (los objetos colaboran entre si)

# tercer_personaje = Personaje(7, "Capitan America", False, 200, False)

# otro_personaje.luchar(tercer_personaje)

# print(personaje.get_nombre())
# personaje.set_nombre("Superior Ironman")
# print(personaje.get_nombre())

# if personaje.set_id(10):
#     print("Esta todo ok")
#     print(personaje.get_nombre())
# else: 
#     print("El id es invalido")

# Herencia ----

# transporte = Transporte(5, 100)

# transporte.mostrar()
# transporte.avanzar()
# transporte.frenar()

# auto = Auto(5, 150, 4)

# print(auto.get_velocidad())

# auto.avanzar()
# auto.mostrar()

avion = Avion(80, 300, 1500)
avion.avanzar()
avion.frenar()
avion.mostrar()



