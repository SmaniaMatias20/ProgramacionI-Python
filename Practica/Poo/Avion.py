from Transporte import Transporte

class Avion(Transporte):
    def __init__(self, cantidad, velocidad, altura):
        super().__init__(cantidad, velocidad)
        self.altura_vuelo = altura

    # Sobreescribiendo metodos de la clase padre
    def frenar(self):
        print("El avion esta descendiendo...")
        super().frenar()

    def avanzar(self):
        print("El avion", end ="")
        super().avanzar()
        print("Nudos por hora")

    def mostrar(self):
        super().mostrar()
        print(f" - Altura {self.altura_vuelo} pies de altura")