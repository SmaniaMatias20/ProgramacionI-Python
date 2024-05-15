import pygame
pygame.font.init()

fuente = pygame.font.Font(None, 50)

BLANCO = (255, 255, 255)
NEGRO  = (  0,   0,   0)
AZUL   = (  0,   0, 255)
VERDE  = ( 32, 255,  32) 

def calcularPerimetro(figura: dict):
    perimetro = figura["base"] * 2 + figura["altura"] * 2
    
    return perimetro
    
def calcularArea(figura: dict):
    area = figura["base"] * figura["altura"]
    
    return area 

def dibujarFigura(ventana: pygame.Surface, figura: dict):
    pygame.draw.rect(ventana, figura["color"], (figura["posicion_x"], figura["posicion_y"], figura["base"], figura["altura"]))
    
def mostrarArea(ventana: pygame.Surface, figura: dict, posicion_x, posicion_y, color, color_fondo):
    area = calcularArea(figura)
    area = fuente.render(f"Area: {area} px", 0, color, color_fondo)
    ventana.blit(area, (posicion_x, posicion_y))

def mostrarPerimetro(ventana: pygame.Surface, figura: dict, posicion_x, posicion_y, color, color_fondo):
    perimetro = calcularPerimetro(figura)
    perimetro = fuente.render(f"Perimetro: {perimetro} px", 0, color, color_fondo)
    ventana.blit(perimetro, (posicion_x, posicion_y)) 
      

def actualizar(ventana: pygame.surface, figura: dict):
    dibujarFigura(ventana, figura)
    mostrarArea(ventana, figura, figura["posicion_x"], figura["posicion_y"] + 200, BLANCO, VERDE)
    mostrarPerimetro(ventana, figura, figura["posicion_x"], figura["posicion_y"] + 250, BLANCO, VERDE)