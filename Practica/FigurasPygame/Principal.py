# Matias Smania 1D

import pygame, sys
from Funciones import *

pygame.init()

ventana = pygame.display.set_mode((800, 500))                                 
pygame.display.set_caption("Figuras Geometricas")

figura = {
    "tipo": "rectangulo", 
    "base": 200,
    "altura": 150, 
    "posicion_x": 100, 
    "posicion_y": 100,
    "color": VERDE
    }

while True: 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    ventana.fill(NEGRO)
    
    actualizar(ventana, figura)
    
    pygame.display.flip()