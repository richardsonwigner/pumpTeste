import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(14, GPIO.OUT)           # set GPIO14 as an output     
try:  
    while True:
        GPIO.input(14)          # This line looks unnecessary, what does it do? 
        sleep(0.5)                  # wait half a second
        GPIO.output(14, 1)  #  set GPIO14 to 1/GPIO.HIGH/True  
    if GPIO.input(14):         # If GPIO14 is TRUE/HIGH
        GPIO.output(14, 0)  # Set GPIO to FALSE/LOW
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()