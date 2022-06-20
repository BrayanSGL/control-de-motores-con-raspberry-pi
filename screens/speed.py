import sys
import pygame
from pygame.locals import *
from .screen import Screen


class Speed(Screen):
    def show(self):
        self.my_lcd.lcd_display_string('Ingrese Vel:', 1)
        return super().show()
        # def show_screen(self):
    #     self.my_lcd.lcd_clear()
    #     self.my_lcd.lcd_display_string('Ingrese Vel:', 1)
    #     while True:
    #         self.screen.fill((255, 255, 255))
    #         for event in pygame.event.get():
    #             if event.type == QUIT:
    #                 pygame.quit()
    #                 sys.exit(0)

    #             if event.type == pygame.KEYDOWN:
    #                 pass
    #         pygame.display.update()
