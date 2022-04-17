import logging
import time
import RPi.GPIO as GPIO

def relay_on():
    GPIO.output(GPIO_CONTROL, False)

    logging.basicConfig(format='%(asctime)s %(message)s', filename='/home/pi/GardenBrain/events.log', level=logging.INFO)
    logging.info('Relay has been manually switched on, from functions.py')

def relay_off():
    GPIO.output(GPIO_CONTROL, True)

    logging.basicConfig(format='%(asctime)s %(message)s', filename='/home/pi/GardenBrain/events.log', level=logging.INFO)
    logging.info('Relay has been manually switched off, from functions.py')


# The main program setup the GPIO
GPIO_CONTROL = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_CONTROL, GPIO.OUT)

# Get input from user to turn on or off relay
while True:
    data = input("Input 'on'/'off' to turn on/off relay, or 'exit' to end ")
    if data == 'on':
        relay_on()
    elif data == 'off':
        relay_off()
    elif data == 'exit':
        # program end, clean up GPIO
        GPIO.cleanup()