import RPi.GPIO as GPIO
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    number = input('Input a number: ')

    if number == 'q':
        raise KeyboardInterrupt

    if int(number) < 0 or int(number) > 255:
        raise ValueError

    GPIO.output(dac, dec2bin(int(number)))

    v = 3.3 * int(number) / 256
    print(f'Expected voltage: {"{:.2f}".format(v)} V')

    sleep(5)
    

except ValueError or ArithmeticError:
    print('Wrong input')

except KeyboardInterrupt:
    print('Program stopped')

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()