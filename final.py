from machine import Pin
import time

red_led = Pin(14, Pin.OUT)  # RED LED
green_led = Pin(13, Pin.OUT)  # GREEN LED
sensor = Pin(27, Pin.IN, Pin.PULL_DOWN)
pump = Pin(26, Pin.OUT)  # pump

print("LIGANDO")

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
