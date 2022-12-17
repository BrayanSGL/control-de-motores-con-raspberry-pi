# Control de Motores con Raspberry Pi 3 y L298N
Este código permite controlar motores utilizando una Raspberry Pi 3 y un controlador L298N. Además, se puede visualizar la información en una pantalla LCD de 16x2.

## Requisitos
- Raspberry Pi 3
- Controlador L298N
- Pantalla LCD 16x2

## Módulos Python
- RPi.GPIO
- time
- I2C_LCD_driver
- pygame

## Uso
Para utilizar este código, es necesario conectar los pines del controlador L298N y la pantalla LCD al Raspberry Pi siguiendo las instrucciones del fabricante.

Una vez conectado, se pueden utilizar las siguientes clases y métodos para controlar los motores y visualizar información en la pantalla:

### Clase Start
La clase Start permite controlar los motores y visualizar información en la pantalla.

#### Método init
Este método inicializa los pines del controlador L298N y la pantalla LCD.

#### Método run
Este método permite controlar los motores y visualizar información en la pantalla. Los parámetros de entrada son:

- speed: velocidad de los motores (entero entre 0 y 100)
- direction: dirección de los motores (1 para avanzar, 0 para retroceder)
- laps: número de vueltas a dar a los motores (entero)

### Clase Screen
La clase Screen permite mostrar diferentes pantallas en la pantalla LCD.

#### Método init
Este método inicializa la pantalla y la pantalla LCD.

#### Método show
Este método muestra la pantalla y maneja los eventos de entrada.

#### Método handle_events
Este método maneja los eventos de entrada y actualiza la pantalla en consecuencia.

### Clases Home, Speed, Direction, Laps
Estas clases representan las diferentes pantallas que se pueden mostrar en la pantalla LCD. Cada una tiene un método show que permite mostrar la pantalla y manejar los eventos de entrada. 
