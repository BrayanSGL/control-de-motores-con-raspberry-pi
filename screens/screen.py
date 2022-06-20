import sys
import pygame
from pygame.locals import *


class Screen():
    def __init__(self, screen, mylcd) -> None:
        self.screen = screen
        self.my_lcd = mylcd
        self.my_lcd.lcd_clear()
        self.is_running = True
        self.input_value = ''

    def __screen(self):
        while self.is_running:
            self.screen.fill((255, 255, 255))
            for event in pygame.event.get():
                self.handle_events(event)

            pygame.display.update()

    def show(self):
        self.__screen()
        return int(self.input_value)

    def handle_events(self, event):
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

    def get_numbers(self, event):
        if event.key == pygame.K_1:
            return '1'

        if event.key == pygame.K_2:
            return '2'

        if event.key == pygame.K_3:
            return '3'

        if event.key == pygame.K_4:
            return '4'

        if event.key == pygame.K_5:
            return '5'

        if event.key == pygame.K_6:
            return '6'

        if event.key == pygame.K_7:
            return '7'

        if event.key == pygame.K_8:
            return '8'

        if event.key == pygame.K_9:
            return '9'

        if event.key == pygame.K_0:
            return '0'

        return ''
