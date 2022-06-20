import sys
import pygame
from pygame.locals import *


class Speed():
    def __init__(self, screen, mylcd) -> None:
        self.screen = screen
        self.my_lcd = mylcd

    def show_screen(self):
        self.my_lcd.lcd_display_string('Ingrese Vel:', 1)
        while True:
            self.screen.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)

                if event.type == pygame.KEYDOWN:
                    pass
            pygame.display.update()
