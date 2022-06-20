import pygame
import sys


class Home():
    def __init__(self, screen,mylcd) -> None:
        self.screen = screen
        self.my_lcd = mylcd
        self.my_lcd.lcd_display_string('Listo entre bb', 1)

    def show_screen(self):
        while True:
            self.screen.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)
