class Transporte:
    def __init__(self, cantidad, velocidad):
        self.cantidad_pasajeros = cantidad
        self.velocidad = velocidad

    def get_velocidad(self):
        return self.velocidad

    def avanzar(self):
        print(f"Avanza a {self.velocidad}", end = "")

    def frenar(self):
        print("Esta frenando")

    def mostrar(self):
        print(f"Pasajeros: {self.cantidad_pasajeros} - velocidad: {self.velocidad}km", end = "")
    