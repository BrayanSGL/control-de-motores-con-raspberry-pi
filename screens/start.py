from sre_constants import IN
import RPi.GPIO as GPIO
import time


class Start():
    def __init__(self, speed, direction, laps, mylcd) -> None:
        self.speed = speed
        self.direction = direction
        self.laps = laps
        self.TIME_FOR_SLEEP = 0.5
        self.IN1 = 11
        self.IN2 = 13
        self.PWM = 18
        self.PULSE = 21
        self.my_lcd = mylcd

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.PWM, GPIO.OUT)
        GPIO.setup(self.PULSE, GPIO.IN)
        pwm=GPIO.PWM(self.PWM,50)
        pwm.start(100)
        # pwm.ChangeDutyCycle(self.speed)


    def run(self):
        self.my_lcd.lcd_clear()
        self.my_lcd.lcd_display_string('Corriendo...', 1)
        
        while self.laps > 0:
            self.my_lcd.lcd_display_string(f'Quedan: {self.laps}', 2)
            if self.direction == 1:
                GPIO.output(self.IN1, GPIO.HIGH)
                GPIO.output(self.IN2, GPIO.LOW)
            else:
                GPIO.output(self.IN1, GPIO.LOW)
                GPIO.output(self.IN2, GPIO.HIGH)
            self.laps -= 1
            #Simulacion de encoder
            time.sleep(2)
        
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
