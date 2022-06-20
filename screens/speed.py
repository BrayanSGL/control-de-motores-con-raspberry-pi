import sys
import pygame
from pygame.locals import *
from .screen import Screen


class Speed(Screen):
        
    def show(self):
        self.my_lcd.lcd_display_string('Ingrese Vel:', 1)
        return super().show()

    def handle_events(self, event):
        super().handle_events(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.is_running = False
            self.input_value += self.get_numbers(event)
        
            self.my_lcd.lcd_display_string(self.input_value, 1,13)