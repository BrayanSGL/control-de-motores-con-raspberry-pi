import I2C_LCD_driver
import pygame
from pygame.locals import *
# Views
from screens.home import Home
from screens.speed import Speed
from screens.direction import Direction
from screens.laps import Laps
from screens.start import Start

# Declaración de constantes y variables
mylcd = I2C_LCD_driver.lcd()


# Función principal del juego
def main():
    speed_val = 0
    direction_val = 1
    laps_val = 0

    menu = 'Home'
    # Se inicializa el juego
    pygame.init()
    pygame.display.set_caption("Cuarta Entrega")
    screen = pygame.display.set_mode((480, 360))
    start = Start(mylcd)

    # Bucle principal
    while True:
        if menu == 'Home':
            home = Home(screen, mylcd, speed_val, direction_val, laps_val)
            menu = home.show_screen()
        elif menu == 'Speed':
            speed = Speed(screen, mylcd)
            speed_val = speed.show()
            menu = 'Home'
        elif menu == 'Direction':
            direction = Direction(screen, mylcd)
            direction_val = direction.show()
            menu = 'Home'
        elif menu == 'Laps':
            laps = Laps(screen, mylcd)
            laps_val = laps.show()
            menu = 'Home'
        elif menu == 'Start':
            start.run(speed_val, direction_val, laps_val)
            menu = 'Home'

    # Este fichero es el que ejecuta el juego principal
if __name__ == '__main__':

    main()
