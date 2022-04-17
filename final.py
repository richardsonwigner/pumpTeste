import utime
from machine import Pin
import time

red_led = Pin(14, Pin.OUT)  # RED LED
green_led = Pin(13, Pin.OUT)  # GREEN LED
sensor = Pin(27, Pin.IN, Pin.PULL_DOWN)
pump = Pin(26, Pin.OUT)  # pump

print()
print(" YYYY MM DD HH MM SS")
dateTime = (input("Enter current date & time: "))+' 0 0'
synchronisedTime = utime.mktime(list(map(int, tuple(dateTime.split(' ')))))
timeDelta = synchronisedTime - int(utime.time())


def timeNow():
    return utime.localtime(utime.time() + timeDelta)


def pump_on():
    red_led.value(1)
    green_led.value(0)
    pump.value(0)
    time.sleep(10)
    print("Pump On - Watering the Plant")


def pump_off():
    red_led.value(0)
    green_led.value(1)
    pump.value(1)
    print("Plant is healthy.")


while True:
    pump_on()
