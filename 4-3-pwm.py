import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)

pwm = GPIO.PWM(21, 60)

pwm.start(0)

try:
    while True:
        dc = int(input('Enter new duty cycle: '))
        pwm.ChangeDutyCycle(dc)
        print(f'Expected voltage: {dc / 100 * 3.3} V')
finally:
    pwm.stop()
    GPIO.output(21, 0)
    GPIO.cleanup()
