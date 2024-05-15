import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Eventos de Teclado")

# x,y = [100,300]

clock = pygame.time.Clock()

pygame.time.set_timer(pygame.USEREVENT, 1000)                # Genera un evento a traves de un temporizador
mensaje = "Hola 1BD"
x,y = [100,100]
font = pygame.font.SysFont("Arial", 30)

tiempo_inicial = pygame.time.get_ticks()                             # Trabajar con el tiempo

player_color = (0,0,255)

# custom_event = pygame.USEREVENT                    # Representa un evento (pygame.USEREVENT representa un numero)
MOVE_UP_EVENT = pygame.USEREVENT
MOVE_DOWN_EVENT = pygame.USEREVENT + 1



bandera = True

while bandera:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False
        # elif event.type == pygame.KEYDOWN:
        #     print(f"Tecla presionada: {event.key}")                # Muestra el valor ASCII de la letra presionada.
        # elif event.type == pygame.KEYUP:
        #     print(f"Tecla liberada: {event.key}")                  # Muestra el valor ASCII de la letra presionada.
        # elif event.type == pygame.KEYDOWN:
        #     nombre = pygame.key.name(event.key)
        #     print(f"Tecla presionada: {nombre}")                   # Muestra el valor char de la letra presionada.
        # elif event.type == pygame.KEYUP:
        #     nombre = pygame.key.name(event.key)
        #     print(f"Tecla liberada: {nombre}")                     # Muestra el valor char de la letra presionada.
        # elif event.type == pygame.MOUSEMOTION:                     # Cuando el mouse se mueve.
        #     # x, y = event.pos
        #     x = event.pos[0]
        #     y = event.pos[1]
        #     print(f"({x}:{y})")                                    # Muestra las coordenadas del mouse.
        # elif event.type == pygame.MOUSEWHEEL:                      # Capturar el movimiento de la ruedita del mouse.
        #     if event.y > 0:
        #         print("Ruedita para arriba")
        #     else:
        #         print("Ruedita para abajo")
        # elif event.type == pygame.MOUSEBUTTONDOWN:                 # Captura el click.
        #     if event.button == 1:
        #         print("Click izquierdo")
        #     elif event.button == 3:
        #         print("Click derecho")
        #     elif event.button == 2:
        #         print("Click ruedita")
        #     else:
        #         print(event.button)                                # Para saber el valor de los botones extras del mouse.

        #----------------EVENTOS PERSONALIZADOS--------------------
        # elif event.type == pygame.KEYDOWN:                           # Ante un evento realizar otro evento.
        #     if event.key == pygame.K_RIGHT:
        #         pygame.event.post(pygame.event.Event(custom_event))  # Agregando el custom_event a la lista de eventos.
        # elif event.type == custom_event:
        #     print("Se presiono la tecla derecha mediante un evento personalizado")

        #--------------EVENTOS PERSONALIZADOS 2.0------------------
    #     elif event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_w:
    #             pygame.event.post(pygame.event.Event(MOVE_UP_EVENT))
    #         elif event.key == pygame.K_s:
    #             pygame.event.post(pygame.event.Event(MOVE_DOWN_EVENT))
    #     elif event.type == MOVE_UP_EVENT:
    #         y -= 10
    #     elif event.type == MOVE_DOWN_EVENT:
    #         y += 10

         
    # pygame.draw.rect(screen, player_color, (x, y, 50, 50))               # Rectangulo
        elif event.type == pygame.USEREVENT:
            x += 10


    screen.fill((0,0,0))     
    texto = font.render(mensaje, True, (255,255,255))
    screen.blit(texto,(x,y))
    pygame.display.update()




    # ---------------------RELOJ---------------------------
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial         # Valores en milisegundos
    print(f"{(tiempo_transcurrido*0.001):.02f}")

    clock.tick(15)        


pygame.quit()
sys.exit()


