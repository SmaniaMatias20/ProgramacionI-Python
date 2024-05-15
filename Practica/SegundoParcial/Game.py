from Modules.Levels.LevelConfig import LevelConfig
from Modules.Gui.GUI_form_main import FormMain
from Modules.Values.Assets import *
from Modules.Values.EColors import *
from pygame.locals import *
import pygame as py
import sys

class Game(LevelConfig):
    def __init__(self, size):
        """
        Brief: Constructor de la clase que inicializa la instancia.

        Descripción:
            Este constructor llama al constructor de la clase base con el tamaño especificado.
            Además, inicializa los atributos 'screen' y 'form_main' con valores predeterminados.

        Parámetros:
            - size: Tamaño de la ventana del juego.

        Retorno:
            Ninguno
        """
        super().__init__(size)
        self.set_background_image(BACKGROUND_IMAGE)
        self.form_main = FormMain(self.screen, 200, 50, 400, 400, EColors.BLACK.value, EColors.WHITE.value, 5, True)
        

    def init(self):
        """
        Brief: Inicializa y ejecuta el bucle principal del juego.

        Descripción:
            Este método inicializa la biblioteca Pygame y ejecuta el bucle principal del juego.
            Controla eventos, actualiza la lógica del juego y mantiene la ejecución hasta que
            se cumple una condición de salida. Luego, finaliza la ejecución y libera los recursos.

        Parametros:
            Ninguno

        Retorno:
            Ninguno
        """
        py.init()

        while self.running:
            self.clock.tick(self.FPS)
            events = py.event.get()
            for event in events:
                if event.type == QUIT:
                    py.quit()
                    sys.exit()

            if self.form_main.exit:
                self.running = False

            self.fill_screen()
            self.form_main.update(events)
            py.display.flip()
        py.quit()