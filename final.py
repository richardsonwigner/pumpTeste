import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Rela 1
GPIO.setup(18, GPIO.OUT)
# Relay 2
GPIO.setup(26, GPIO.OUT)

try:
    while True:
        GPIO.output(18, GPIO.LOW)
        print('Relay 1 ON')
        time.sleep(1)
        
finally:
    GPIO.cleanup()