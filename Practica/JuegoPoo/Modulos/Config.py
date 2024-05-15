import pygame as py

FPS = 60

class Config:
    def __init__(self, size, FPS, caption= "Tittle", icon= ""):
        py.mixer.init()
        self.size = size
        self.screen = py.display.set_mode(size)
        self.FPS = FPS
        self.running = True
        self.clock = py.time.Clock()
        self.set_caption(caption)
        

    def set_caption(self, caption):
        py.display.set_caption(caption)

    def set_icon(self, icon):
        pass

    def set_fps(self, FPS):
        self.FPS = FPS

    def set_music(self, music):
        self.music = py.mixer.Sound(music)
        self.music.set_volume(0.2)
        self.play_music()
    
    def play_music(self):
        self.music.play()

    def stop_music(self):
        self.music.stop()


    def set_volume(self, volume):
        self.music.set_volume(volume)

    def set_background_image(self):
        pass

    def set_fuente(self):
        pass

    def fill_screen(self, color):
        if color != None:
            self.screen.fill(color)
        else:
            pass
    
