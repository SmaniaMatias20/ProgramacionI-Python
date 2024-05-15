class Personaje:
    def __init__(self, id: int, nombre: str, puede_volar: bool, poder: int, usa_nano: bool):
        self.__id = id                      
        self.__nombre = nombre            
        self.__puede_volar = puede_volar    
        self.__usa_nano = usa_nano
        self.__poder = poder

        # __init__() ---> Metodo constructor.
        # self.id ---> Atributo de la clase.
        # Atributo publico
        # Atributo privado __
        # Atributo protegido _
        
    def retornar_descripcion(self):
        descripcion = f"{self.id}-{self.__nombre}-{self.__puede_volar}-{self.__usa_nano}"
        return descripcion
    
    def luchar(self, otro_personaje):
        print(f"{self.__nombre} VS {otro_personaje.__nombre}")
        if self.__poder > otro_personaje.__poder:
            print(f"Gano: {self.__nombre}")
        elif self.__poder < otro_personaje.__poder:
            print(f"Gano: {otro_personaje.__nombre}")
        else:
            print("Hubo empate")

    # Getters y Setters
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre.strip().title()

    def set_id(self, id):
        retorno = False
        if id > 0:
            self.__id = id
            retorno = True
        
        return retorno
        

        


'''
Cuatro Pilares de POO

- Abstraccion
- Herencia
- Encapsulamiento
- Polimorfismo
'''


