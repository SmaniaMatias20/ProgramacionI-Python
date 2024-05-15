# Matias Smania 1D

import pygame, sys

pygame.init()

BLANCO = (255, 255, 255)
NEGRO  = (  0,   0,   0)
AZUL   = (  0,   0, 255)

ventana = pygame.display.set_mode((800, 500))                                 
pygame.display.set_caption("Diccionarios e Imagenes")

fuente = pygame.font.Font(None, 70)

imagen_michi = pygame.image.load("imagenes/michi.jpeg")
imagen_perro = pygame.image.load("imagenes/perro.jpg")
imagen_tucan = pygame.image.load("imagenes/tucan.jpg")

imagen_michi = pygame.transform.scale(imagen_michi, (80, 80))
imagen_perro = pygame.transform.scale(imagen_perro, (80, 80))
imagen_tucan = pygame.transform.scale(imagen_tucan, (80, 80))

primera_mascota = {"nombre" : "Michi", "edad": 5, "imagen": imagen_michi}
segunda_mascota = {"nombre" : "Perro", "edad": 3, "imagen": imagen_perro}
tercera_mascota = {"nombre" : "Tucan", "edad": 7, "imagen": imagen_tucan}
lista_mascotas = [primera_mascota, segunda_mascota, tercera_mascota]                               
    
ubicacion_y = 150

while True: 

    #Para cerrar la ventana del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    ventana.fill(NEGRO)

    for mascota in lista_mascotas:
     
        nombre = fuente.render(mascota["nombre"], 0, BLANCO, AZUL)
        edad = mascota["edad"]
        edad = fuente.render(f"{edad}", 0, BLANCO, AZUL) 
        imagen = mascota["imagen"]
        
        ventana.blit(nombre, (100, ubicacion_y))
        ventana.blit(edad, (300, ubicacion_y))
        ventana.blit(imagen, (500, ubicacion_y))
        ubicacion_y += 100

    ubicacion_y = 150
    
    pygame.display.flip()