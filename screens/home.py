import pygame
import sys


class Home():
    def __init__(self, screen, mylcd) -> None:
        self.screen = screen
        self.my_lcd = mylcd
        self.OPTIONS = [
            {
                'option': 1,
                'text': 'Velocidad'
            },
            {
                'option': 2,
                'text': 'Sentido'
            },
            {
                'option': 3,
                'text': '# Vueltas'
            },
            {
                'option': 4,
                'text': 'Iniciar'
            }
        ]
        self.selected = 0

    def __show_menu(self, is_going_down):

        self.my_lcd.lcd_clear()
        new_options = self.OPTIONS[self.selected -
                                   is_going_down:self.selected+2-is_going_down]

        self.my_lcd.lcd_display_string(new_options[0].get('text'), 1)
        self.my_lcd.lcd_display_string(new_options[1].get('text'), 2)
        self.my_lcd.lcd_display_string('*', is_going_down+1, 15)
        print(self.selected)

    def show_screen(self):
        self.__show_menu(0)
        while True:
            self.screen.fill((255, 255, 255))
            # 2.- Se comprueban los eventos
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)

                if event.type == pygame.KEYDOWN:
                    # Teclas de arriba y abajo

                    if event.key == pygame.K_DOWN and len(self.OPTIONS) > self.selected+1:
                        self.selected += 1
                        self.__show_menu(1)
                    elif event.key == pygame.K_UP and 0 < self.selected:
                        self.selected -= 1
                        self.__show_menu(0)
                    # Enter
