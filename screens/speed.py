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
                if int(self.input_value) % 10 == 0 and int(self.input_value)<=100:
                    self.is_running = False
                else:
                    self.input_value = ''

            elif event.key == pygame.K_DELETE:
                self.input_value.pop()

            else:
                self.input_value += self.get_numbers(event)

            self.my_lcd.lcd_display_string(self.input_value, 1, 13)
