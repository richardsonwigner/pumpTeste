import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
GPIO.setmode(GPIO.BOARD)             # choose BCM or BOARD  
GPIO.setup(18, GPIO.OUT)           # set GPIO18 as an output     
try:  
    while True:
        GPIO.input(18)          # This line looks unnecessary, what does it do? 
        sleep(0.5)                  # wait half a second
        GPIO.output(18, 1)  #  set GPIO18 to 1/GPIO.HIGH/True  
    if GPIO.input(18):         # If GPIO18 is TRUE/HIGH
        GPIO.output(18, 0)  # Set GPIO to FALSE/LOW
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()