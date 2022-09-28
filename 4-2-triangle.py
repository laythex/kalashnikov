import RPi.GPIO as GPIO
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


try:
    p = int(input('Enter period: '))
    n, k = 0, 1
    while True:
        GPIO.output(dac, dec2bin(n))
        sleep(p / 256 / 2)
        n += k
        if n == 0 or n == 255:
            k *= -1
except ValueError or ArithmeticError:
    print('Wrong input')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()