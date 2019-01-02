from RPLCD import CharLCD
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
import requests
import time
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23], numbering_mode=GPIO.BOARD)
lcd.clear()


while (1):

    r =requests.get('https://api.thingspeak.com/apps/thinghttp/send_request?api_key=FC2SH6OCE1E3TGAJ')
    #valuestart = r.text.find("value")
    #valueend = r.text.find("/span")                     
    #value = r.text[valuestart+7:valueend-1]

    per =requests.get('https://api.thingspeak.com/apps/thinghttp/send_request?api_key=GAXDKF8DG6IWFPSF')
    #percentstart = per.text.find("--q")
    #percentend = per.text.find("/span")                     
    #percent = per.text[percentstart+5:percentend-1]

    


    
    lcd.cursor_pos = (1,0)
    lcd.write_string(r.text.replace(" ",""))
    print(r.text)
    lcd.cursor_pos = (1,0)
    print(per.text)
    lcd.write_string(per.text)

    #lcd.cursor_pos = (0,10)
    #lcd.write_string(str(eth))
    time.sleep(5)





