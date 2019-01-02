import RPi.GPIO as GPIO
import time
import datetime
import sys, os

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3,GPIO.OUT)
#GPIO.setup(7,GPIO.IN)

p= GPIO.PWM(3,50)
p.start(0)

path = '/home/pi/Desktop/Python/Smart_garden/Times_watered.txt'
file = open(path,'r')
file.read()

try:
    while True:
        if (mcp.read_adc(0)>550):
            time.sleep(2)
            water=mcp.read_adc(0)
            per = round(abs((water-1023)/1023)*100,1)
            if (water>550):             
                print("DRY: " + str(per) + "%")
                message =  datetime.datetime.now().strftime("%m-%d-%y__%H:%M")
                path = "/home/pi/Desktop/Python/Smart_garden/Times_watered.txt"
                with open(path,"a") as myfile:
                    myfile.write("\n" + str(message))
                os.system('./camera.sh')
                p.ChangeDutyCycle(2.5)
                time.sleep(.75)
                p.ChangeDutyCycle(13)
                time.sleep(10)
            
        else:
            per = round(abs((mcp.read_adc(0)-1023)/-1023)*100,1)
            print("wet: " + str(per) + "%")            
            
        time.sleep(4)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    
    
