import RPi.GPIO as GPIO
import time


class Start():
    def __init__(self, speed, direction, laps) -> None:
        self.speed = speed
        self.direction = direction
        self.laps = laps
        self.TIME_FOR_SLEEP = 0.5
        self.IN1 = 11
        self.IN2 = 13
        self.PWM = 18

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.PWM, GPIO.OUT)

    def run(self):
        while self.laps > 0:
            if self.direction == 1:
                GPIO.output(self.IN1, GPIO.HIGH)
                GPIO.output(self.IN2, GPIO.LOW)
            else:
                GPIO.output(self.IN1, GPIO.LOW)
                GPIO.output(self.IN2, GPIO.HIGH)
            self.laps -= 1
            time.sleep(2)
        
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)
