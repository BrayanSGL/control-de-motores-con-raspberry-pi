import sys
import pygame
from pygame.locals import *


class Screen():
    def __init__(self, screen, mylcd) -> None:
        self.screen = screen
        self.my_lcd = mylcd
        self.my_lcd.lcd_clear()
        self.is_running = True

    def __screen(self):
        while self.is_running:
            self.screen.fill((255, 255, 255))
            for event in pygame.event.get():
                self.handle_events(event)

            pygame.display.update()

    def show(self):
        self.__screen()

    def handle_events(self, event):
        pass
        # if event.type == QUIT:
        #     pygame.quit()
        #     sys.exit(0)

        # if event.type == pygame.KEYDOWN:
        #     pass
