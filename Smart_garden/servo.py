import RPi.GPIO as GPIO
import time
import datetime


GPIO.setmode(GPIO.BOARD)

GPIO.setup(3,GPIO.OUT)

p= GPIO.PWM(3,50)
p.start(0)

   
    
       
try:
    
    while True:
        x= int(input("1 for water "))

        y= float(input("Amount of time "))
        if 1==x:
            p.ChangeDutyCycle(2.5)
            time.sleep(y)
            p.ChangeDutyCycle(13)
    
        
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()