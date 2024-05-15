from Transporte import Transporte

class Auto(Transporte):
    def __init__(self, cantidad, velocidad, ruedas):
        super().__init__(cantidad, velocidad)
        self.cantidad_ruedas = ruedas

    # Sobreescribiendo metodos de la clase padre
    def avanzar(self):
        print("El auto", end ="")
        super().avanzar()
        print("KM por hora")
    

    def mostrar(self):
        super().mostrar()
        print(f" - Cantidad de ruedas {self.cantidad_ruedas}")