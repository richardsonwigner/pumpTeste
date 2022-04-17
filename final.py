import time
import RPi.GPIO as GPIO
import datetime
import sqlite3
GPIO.setmode(GPIO.BCM)
#control relay
GPIO.setup(18, GPIO.OUT) 
GPIO.output(18,GPIO.HIGH)
#Led output
GPIO.setup(15, GPIO.OUT)
GPIO.output(15, GPIO.HIGH)  
#push button
GPIO.setup(14, GPIO.IN)
led = False

GPIO.output(18,GPIO.HIGH)


while True:
    print("RELAY DESLIGADO")
    time.sleep(0.5)

def my_callback(channel):  	#manual watering
	input_state = GPIO.input(14)
	if input_state == False:
		print('Manual watering')
		GPIO.output(15,GPIO.LOW)	#LED on
		GPIO.output(18,GPIO.LOW)	#RELAY on
		time.sleep(0.5)
	else:
		GPIO.output(15,GPIO.HIGH)	#LED off
		GPIO.output(18,GPIO.HIGH)	#RELAY off
		#write log
		now = datetime.datetime.now()
		timeString = now.strftime("%Y-%m-%d %H:%M:%S")
GPIO.add_event_detect(14, GPIO.RISING, callback=my_callback) 
try:
	while True:
		a=1
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
	GPIO.cleanup()