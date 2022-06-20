import pygame
from pygame.locals import *
from .screen import Screen


class Direction(Screen):

    def show(self):
        self.my_lcd.lcd_display_string('   Sentido:', 1)
        self.my_lcd.lcd_display_string('1. Der  |  2.Izq', 2)
        return super().show()

    def handle_events(self, event):
        super().handle_events(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if int(self.input_value) == 1 or int(self.input_value) == 2:
                    self.is_running = False
                else:
                    self.input_value = ''

            elif event.key == pygame.K_BACKSPACE and len(self.input_value) > 0:
                self.input_value = self.input_value[:-1]

            else:
                if len(self.input_value) == 1:
                    return
                self.input_value += self.get_numbers(event)

            self.my_lcd.lcd_display_string('   ', 1, 12)
            self.my_lcd.lcd_display_string(self.input_value, 1, 12)
