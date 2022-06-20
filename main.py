import I2C_LCD_driver
import random
import pygame
import sys
import time
from pygame.locals import *
# Views
from screens.home import Home

# Declaración de constantes y variables
WHITE = (255, 255, 255)
mylcd = I2C_LCD_driver.lcd()
numero = ''
valor = 0
menu = ''

speed = 0

# Funcion para mostrar el menu con Scroll


# Pantallas del menu
# def pantalla_error():

# def pantalla_pausa():

def pantalla_velocidad(value):
    global speed
    mylcd.lcd_clear()
    mylcd.lcd_display_string('Ingrese la', 1, 3)
    mylcd.lcd_display_string('velocidad -> '+str(value)+'%', 2)
    speed = value


# Función principal del juego
def main():
    global selected
    global numero
    global speed
    menu = 'Home'
    numeroVel = '0'
    # Se inicializa el juego
    pygame.init()
    pygame.display.set_caption("Cuarta Entrega")
    screen = pygame.display.set_mode((480, 360))

    # Bucle principal
    while True:

        # 1.- Se dibuja la pantalla
        # screen.fill(WHITE)
        if menu == 'Home':
            home = Home(screen, mylcd)
    # 3.- Se actualiza la pantalla
        pygame.display.update()


# Este fichero es el que ejecuta el juego principal
if __name__ == '__main__':

    main()
