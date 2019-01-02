import RPi.GPIO as GPIO
import time
import datetime
import sys, os

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3,GPIO.OUT)
GPIO.setup(7,GPIO.IN)

p= GPIO.PWM(3,50)
p.start(0)

path = '/home/pi/Desktop/Python/Smart_garden/Times_watered.txt'
file = open(path,'r')
file.read()

try:
    while True:
        if GPIO.input(7):
            print("DRY")
            message =  datetime.datetime.now().strftime("%m-%d-%y__%H:%M")
            path = "/home/pi/Desktop/Python/Smart_garden/Times_watered.txt"
            with open(path,"a") as myfile:
                myfile.write("\n" + str(message))
            p.ChangeDutyCycle(2.5)
            time.sleep(1)
            p.ChangeDutyCycle(13)
            time.sleep(3600)
            
        else:           
            print("wet")
            
            
        time.sleep(10)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    
    