from Modulos.Characters.Falling_object import FallingObject
from Modulos.Characters.Object import Object


class Heroe(Object):
    def __init__(self, size, position = (0, 0), speed = 5) -> None:
        super().__init__(size, position)
        self.set_speed(speed)
        self.point = 0

    def move_right(self, top_right):
        new_x = self.rect.x + self.speed
        if new_x <= top_right - self.rect.width:
            super().move_right()

    def move_left(self, top_left):
        new_x = self.rect.x - self.speed
        if new_x >= top_left:
            super().move_left()

    def collide_with_falling_objects(self, falling_objects: list['FallingObject']):
        for fo in falling_objects:
            if self.rect.colliderect(fo.rect):
                fo.set_random_position()
                self.collide_fo_effects()
                self.point += 1
            
            
    def collide_fo_effects(self):
        pass