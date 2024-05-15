import pygame, sys
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Matias
Apellido: Smania

Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        # self.btn_cargar = customtkinter.CTkButton(
        #     master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        # self.btn_cargar.grid(row=2, padx=20, pady=20,
        #                      columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista = [8,22,30,-7,9,2,10,-2,0,0,12,0,0,3,1,15,100,-29,-30,-25,-2,]

    # def btn_comenzar_ingreso_on_click(self):
        
    #     numero_ingresado = ""

    #     while numero_ingresado != None:
    #         numero_ingresado = prompt("Numero", "Ingrese un numero")
            
    #         if numero_ingresado == None:
    #             break

    #         if numero_ingresado == "" or numero_ingresado.isalpha():
    #             continue
            
    #         numero_ingresado = int(numero_ingresado)

    #         self.lista.append(numero_ingresado)

    def btn_mostrar_estadisticas_on_click(self):

        # Deberán elegir cualquier ejercicio del ingreso, a partir del cual visualizarán los resultados de las estadísticas solicitadas en una ventana de pygame.
        # La ventana deberá contar con un icono, y un título acorde al programa.
        # La ventana deberá tener un color de relleno.
        # Los resultados se tendrán que ver con un color y un background que haga contraste con el fondo de la ventana.
        # Por ejemplo:

        acumulador_positivos = 0
        acumulador_negativos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_cero = 0
        minimo_negativo = 0
        maximo_positivo = 0
        promedio_negativos = 0

        for numero in self.lista:

            if numero > 0:

                if contador_positivos == 0:
                    maximo_positivo = numero

                if numero > maximo_positivo:
                    maximo_positivo = numero

                acumulador_positivos += numero
                contador_positivos += 1
            elif numero < 0:

                if contador_negativos == 0:
                    minimo_negativo = numero

                if numero < minimo_negativo:
                    minimo_negativo = numero

                acumulador_negativos += numero
                contador_negativos += 1
            else:
                contador_cero += 1  

        if contador_negativos != 0:
            promedio_negativos = acumulador_negativos // contador_negativos
        else:
            promedio_negativos = 0    
        
        # alert("Trabajo Practico", f"""

        # Punto A: La suma acumulada de los numeros negativos es: {acumulador_negativos}
        # \nPunto B: La suma acumulada de los numeros positivos es: {acumulador_positivos}
        # \nPunto C: La cantidad de numeros positivos es: {contador_positivos}
        # \nPunto D: La cantidad de numeros negativos es: {contador_negativos}
        # \nPunto E: La cantidad de 0(ceros) es: {contador_cero}
        # \nPunto F: El minimo de los negativos es: {minimo_negativo}
        # \nPunto G: El maximo de los positivos es: {maximo_positivo}
        # \nPunto H: El promedio de los numeros negativos es: {promedio_negativos}

        # """)

        pygame.init()
        
        ventana = pygame.display.set_mode((1250, 700))                                 
        pygame.display.set_caption("Ejercicio con listas en Pygame") 
        icono = pygame.image.load("home.png")                                       
        pygame.display.set_icon(icono) 

        fuente = pygame.font.SysFont("Arial", 30)
        punto_a = fuente.render(f"Punto A: La suma acumulada de los numeros negativos es: {acumulador_negativos}",0,(255,255,255)) 
        punto_b = fuente.render(f"Punto B: La suma acumulada de los numeros positivos es: {acumulador_positivos}",0,(255,255,255)) 
        punto_c = fuente.render(f"Punto C: La cantidad de numeros positivos es: {contador_positivos}",0,(255,255,255)) 
        punto_d = fuente.render(f"Punto D: La cantidad de numeros negativos es: {contador_negativos}",0,(255,255,255)) 
        punto_e = fuente.render(f"Punto E: La cantidad de 0(ceros) es: {contador_cero}",0,(255,255,255)) 
        punto_f = fuente.render(f"Punto F: El minimo de los negativos es: {minimo_negativo}",0,(255,255,255)) 
        punto_g = fuente.render(f"Punto G: El maximo de los positivos es: {maximo_positivo}",0,(255,255,255)) 
        punto_h = fuente.render(f"Punto H: El promedio de los numeros negativos es: {promedio_negativos}",0,(255,255,255)) 

        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            ventana.fill((0,0,0))
            ventana.blit(punto_a,(100,150))
            ventana.blit(punto_b,(100,200))
            ventana.blit(punto_c,(100,250))
            ventana.blit(punto_d,(100,300))
            ventana.blit(punto_e,(100,350))
            ventana.blit(punto_f,(100,400))
            ventana.blit(punto_g,(100,450))
            ventana.blit(punto_h,(100,500))
        
            pygame.display.flip()
            


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
