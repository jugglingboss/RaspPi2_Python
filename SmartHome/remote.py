import paho.mqtt.client as mqtt
import time
import subprocess
# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/tv")

def on_message(client, userdata, msg):
  if msg.payload.decode() == "power":
    print("power on")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_POWER"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_POWER"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_POWER"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_POWER"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_POWER"])
      
  if msg.payload.decode() == "volumeup":
    print("volumeup")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_VOLUMEUP"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_VOLUMEUP"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_VOLUMEUP"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_VOLUMEUP"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_VOLUMEUP"])


  if msg.payload.decode() == "volumedown":
    print("volumedown")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_VOLUMEDOWN"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_VOLUMEDOWN"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_VOLUMEDOWN"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_VOLUMEDOWN"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_VOLUMEDOWN"])
  
  if msg.payload.decode() == "xbox":
    print("xbox routine")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_POWER"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_POWER"])
    time.sleep(.05)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_HOME"])
    time.sleep(.05)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_HOME"])
    time.sleep(.05)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_RIGHT"])
    time.sleep(.05)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_RIGHT"])
    time.sleep(.05)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_OK"])
    
  if msg.payload.decode() == "pc":
    print("pc routine")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_POWER"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_POWER"])
    time.sleep(.05)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_HOME"])
    time.sleep(.05)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_HOME"])
    time.sleep(.05)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_RIGHT"])
    time.sleep(.05)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_OK"])
 
  if msg.payload.decode() == "chromecast":
    print("chrome cast routine")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_POWER"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_POWER"])
    time.sleep(.05)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_HOME"])
    time.sleep(.05)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_HOME"])
    time.sleep(.05)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_RIGHT"])
    time.sleep(.05)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_RIGHT"])
    time.sleep(.05)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_RIGHT"])
    time.sleep(.05)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_OK"])
  
  if msg.payload.decode() == "netflix":
    print("netflix routine")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_POWER"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_POWER"])
    time.sleep(.05)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_N"])
    #time.sleep(2)
    #rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_OK"])
    
  if msg.payload.decode() == "vudu":
    print("vudu routine")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_POWER"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_POWER"])
    time.sleep(.05)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_V"])

  if msg.payload.decode() == "play":
    print("play/pause")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "MYTV", "KEY_PLAY"])
  
  if msg.payload.decode() == "LED":
    print("LED and turn on FADE7")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "LONGLED", "KEY_POWER"])
    time.sleep(.1)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "LONGLED", "KEY_F"])

  if msg.payload.decode() == "LEDplay":
    print("LED play")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "LONGLED", "KEY_PLAY"])

  if msg.payload.decode() == "red":
    print("LED red")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "LONGLED", "KEY_R"])

  if msg.payload.decode() == "green":
    print("LED green")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "LONGLED", "KEY_G"])
    
  if msg.payload.decode() == "blue":
    print("LED blue")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "LONGLED", "KEY_B"])
    
  if msg.payload.decode() == "white":
    print("LED white")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "LONGLED", "KEY_W"])
    
  if msg.payload.decode() == "jump":
    print("LED jump7")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "LONGLED", "KEY_J"])
    
  if msg.payload.decode() == "fade":
    print("LED FADE7")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "LONGLED", "KEY_F"])
    
  if msg.payload.decode() == "flash":
    print("LED flash")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "LONGLED", "KEY_F1"])
    
  if msg.payload.decode() == "quick":
    print("LED quick")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "LONGLED", "KEY_Q"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "LONGLED", "KEY_Q"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "LONGLED", "KEY_Q"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "LONGLED", "KEY_Q"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "LONGLED", "KEY_Q"])
    
  if msg.payload.decode() == "slow":
    print("LED slow")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "LONGLED", "KEY_S"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "LONGLED", "KEY_S"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "LONGLED", "KEY_S"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "LONGLED", "KEY_S"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "LONGLED", "KEY_S"])
    
  
  
    
client = mqtt.Client()
client.connect("192.168.1.9",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
