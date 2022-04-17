import time
import RPi.GPIO as GPIO

def relay_on():
    print("RELAY LIGADO")
    GPIO.output(GPIO_CONTROL, False)
def relay_off():
    print("RELAY DESLIGADO")
    GPIO.output(GPIO_CONTROL, True)



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