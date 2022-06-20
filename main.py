import I2C_LCD_driver
import pygame
from pygame.locals import *
# Views
from screens.home import Home
from screens.speed import Speed

# Declaración de constantes y variables
WHITE = (255, 255, 255)
mylcd = I2C_LCD_driver.lcd()
numero = ''
valor = 0
menu = ''
speed_val = 0

# Función principal del juego


def main():
    menu = 'Home'
    # Se inicializa el juego
    pygame.init()
    pygame.display.set_caption("Cuarta Entrega")
    screen = pygame.display.set_mode((480, 360))

    # Bucle principal
    while True:

        # 1.- Se dibuja la pantalla
        # screen.fill(WHITE)
        if menu == 'Home':
            home = Home(screen, mylcd,speed_val)
            menu = home.show_screen()
        elif menu == 'Speed':
            speed = Speed(screen, mylcd)
            speed_val = speed.show()
            
            menu = 'Home'

    # Este fichero es el que ejecuta el juego principal
if __name__ == '__main__':

    main()
