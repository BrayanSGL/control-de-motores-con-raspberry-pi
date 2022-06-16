import I2C_LCD_driver
import random, pygame, sys, time
from pygame.locals import *

# Declaración de constantes y variables
WHITE = (255, 255, 255)
mylcd = I2C_LCD_driver.lcd()
OPTIONS = [
	{
		'option':1,
		'text': 'Velocidad'
	},
	{
		'option':2,
		'text': 'Sentido'
	},
	{
		'option':3,
		'text': '# Vueltas'
	},
	{
		'option':4,
		'text': 'Iniciar'
	}
]
selected = 0
numero = ''
valor = 0
menu = ''

speed=0

# Funcion para mostrar el menu con Scroll
def mostrar_menu(is_going_down):
	
	mylcd.lcd_clear()
	new_options = OPTIONS[selected-is_going_down:selected+2-is_going_down]

	mylcd.lcd_display_string(new_options[0].get('text'), 1)
	mylcd.lcd_display_string(new_options[1].get('text'), 2) 
	mylcd.lcd_display_string('*', is_going_down+1, 15)
	print(selected)

#Pantallas del menu
#def pantalla_error():
	
#def pantalla_pausa():

def pantalla_velocidad(value):
	global speed
	mylcd.lcd_clear()
	mylcd.lcd_display_string('Ingrese la', 1,3)
	mylcd.lcd_display_string('velocidad -> '+str(value)+'%', 2)
	speed=value



# Función principal del juego
def main():
	global selected
	global numero
	global menu
	global speed
	numeroVel='0'
	# Se inicializa el juego
	pygame.init()
	pygame.display.set_caption("Cuarta Entrega")
	screen = pygame.display.set_mode((480,360))  
	mostrar_menu(0)
	
	# Bucle principal
	while True:

		# 1.- Se dibuja la pantalla
		screen.fill(WHITE)

		# 2.- Se comprueban los eventos
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit(0)
		  
			if event.type == pygame.KEYDOWN:
				#Teclas de arriba y abajo
				print(speed)
				if event.key == pygame.K_DOWN and len(OPTIONS)>selected+1:
					selected+=1
					mostrar_menu(1)
				elif event.key == pygame.K_UP and 0<selected:
					selected-=1
					mostrar_menu(0)
				#Enter
				if menu == '' and event.key == pygame.K_RETURN:
					menu = OPTIONS[selected].get('text')
					#print(menu)
				#Pasamos a los números
				if menu != '':
					if event.key == pygame.K_1:
						numero = '1'
					if event.key == pygame.K_2:
						numero = '2'
					if event.key == pygame.K_3:
						numero = '3'
					if event.key == pygame.K_4:
						numero = '4'
					if event.key == pygame.K_5:
						numero = '5'
					if event.key == pygame.K_6:
						numero = '6'
					if event.key == pygame.K_7:
						numero = '7'
					if event.key == pygame.K_8:
						numero = '8'
					if event.key == pygame.K_9:
						numero = '9'
					if event.key == pygame.K_0:
						numero = '0';
					#Opcion de velocidad
					if menu == OPTIONS[0].get('text'):
						if len(numeroVel)==2:
							numeroVel=numero
						else:
							numeroVel += numero
						
						#print(numeroVel)
						pantalla_velocidad(int(numeroVel))
						print(speed)
						if event.key == pygame.K_RETURN and len(numeroVel)>1:
							menu=''
							mostrar_menu(0)
							
						

    # 3.- Se actualiza la pantalla
		pygame.display.update()

# Este fichero es el que ejecuta el juego principal
if __name__ == '__main__':
	
	main()
