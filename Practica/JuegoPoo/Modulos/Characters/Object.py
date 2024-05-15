import pygame as py
from Modulos.Characters.Values.Eorientation import Eorientation

class Object:
    def __init__(self, size_surface, position):
        # self.set_speed(0)

        self.image = py.Surface(size_surface) 
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

        self.direction = Eorientation.IDLE
        

    def set_speed(self, speed):
        self.speed = speed


    def move_right(self):
        self.direction = Eorientation.RIGHT
        self.move()
    
    def move_left(self):
        self.direction = Eorientation.LEFT
        self.move()
    
    def move_up(self):
        self.direction = Eorientation.UP
        self.move()
    
    def move_down(self):
        self.direction = Eorientation.DOWN
        self.move()

    def stop(self):
        self.direction = Eorientation.IDLE
        self.move()

    def move(self):

        if self.direction == Eorientation.LEFT:
            self.rect.x -= self.speed
        elif self.direction == Eorientation.RIGHT:
            self.rect.x += self.speed
        elif self.direction == Eorientation.UP:
            self.rect.y -= self.speed
        elif self.direction == Eorientation.DOWN:
            self.rect.y += self.speed
        elif self.direction == Eorientation.IDLE:
            pass
        else:
            raise ValueError('Invalid direction')
        
