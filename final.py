import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Rela 1
GPIO.setup(5, GPIO.OUT)
# Relay 2
GPIO.setup(6, GPIO.OUT)

try:
    while True:
        # GPIO.output(18, GPIO.HIGH)
        # print('Relay 1 ON')
        # time.sleep(1)
        # GPIO.output(26, GPIO.HIGH)
        # print('Relay 2 ON')
        # time.sleep(1)
        # GPIO.output(18, GPIO.LOW)
        # print('Relay 1 OFF')
        # time.sleep(1)
        # GPIO.output(26, GPIO.LOW)
        # print('Relay 2 OFF')
        # time.sleep(1)


        GPIO.output(5, GPIO.LOW)
        print('RELAY 1 ON')
        time.sleep(2)
        GPIO.output(5, GPIO.HIGH)
        print('RELAY 1 OFF')
        time.sleep(2)
        GPIO.output(6, GPIO.LOW)
        print('RELAY 2 ON')
        time.sleep(2)
        GPIO.output(6, GPIO.HIGH)
        print('RELAY 2 OFF')
        time.sleep(2)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        print('RELAY 1 & 2 ON')
        time.sleep(3)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(6, GPIO.HIGH)
        print('RELAY 1 & 2 OFF')       
        time.sleep(3)
        
finally:
    GPIO.cleanup()