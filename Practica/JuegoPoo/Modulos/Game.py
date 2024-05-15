from Modulos.Characters.Falling_object import FallingObject
from Modulos.Characters.Heroe import Heroe
from Modulos.Colors import *
from Modulos.Config import Config
import pygame as py

from Modulos.Colors import BLANCO


# https://github.com/mrampi/pygame_poo


class Game(Config):
    def __init__(self, size, FPS, caption= "Tittle", icon = ""):
        super().__init__(size, FPS, caption, icon)               # Llamamos al constructor de la clase padre.
        self.set_heroe()
        self.set_falling_object(28)


    def set_falling_object(self, size):
        self.falling_object = FallingObject.create_list(size, self.size)

    def set_heroe(self):
        x = self.size[0] // 2
        y = self.size[1] - 160
        self.heroe = Heroe((50, 75), (x, y), 10)

    def move_heroe(self):
        if self.pressed_keys[py.K_RIGHT]:
            self.heroe.move_right(self.size[0])
        elif self.pressed_keys[py.K_LEFT]:
            self.heroe.move_left(0)
        elif self.pressed_keys[py.K_UP]:
            self.heroe.move_up()
        elif self.pressed_keys[py.K_DOWN]:
            self.heroe.move_down()
        else:
            self.heroe.stop()

    def blit_falling_object(self):
        for fo in self.falling_object:
            fo.move_down()
            self.screen.blit(fo.image, fo.rect)

    def blit_heroe(self):
        self.screen.blit(self.heroe.image, self.heroe.rect)

    def get_pressed(self):
        self.pressed_keys = py.key.get_pressed()  


    def check_collides(self):
        self.heroe.collide_with_falling_objects(self.falling_object)
        self.show_score(self.heroe.point)


    def init(self):
        py.init()
    
        while self.running:
            self.clock.tick(self.FPS)

            self.fill_screen((PURPURA))

            for event in py.event.get():
                if event.type == py.QUIT:
                    self.running = False
            
        
            self.get_pressed()

            self.move_heroe()
            self.blit_heroe()
            self.check_collides()
            self.blit_falling_object()

            

            py.display.flip()

        py.quit()
    
    def show_score(self, text):
        font = py.font.SysFont("Arial", 30)
        text = font.render(F"Score: {text}", True, BLANCO)
        self.screen.blit(text, (0,0))