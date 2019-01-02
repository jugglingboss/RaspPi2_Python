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
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_POWER"])
  
  if msg.payload.decode() == "volumeup":
    print("volumeup")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEUP"])
  
  if msg.payload.decode() == "volumetenup":
    print("volumetenup")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEUP"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEUP"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEUP"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEUP"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEUP"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEUP"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEUP"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEUP"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEUP"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEUP"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEUP"])

  if msg.payload.decode() == "volumedown":
    print("volumedown")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEDOWN"])
  
  if msg.payload.decode() == "volumetendown":
    print("volumetendown")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEDOWN"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEDOWN"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEDOWN"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEDOWN"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEDOWN"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEDOWN"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEDOWN"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEDOWN"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEDOWN"])
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_VOLUMEDOWN"])

  
  if msg.payload.decode() == "channelup":
    print("channelup")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_CHANNELUP"])
  
  if msg.payload.decode() == "channeldown":
    print("channeldown")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_CHANNELDOWN"])
  
  if msg.payload.decode() == "up":
    print("up")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_UP"])
 
  if msg.payload.decode() == "down":
    print("down")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_DOWN"])
 
  if msg.payload.decode() == "enter":
    print("enter")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_ENTER"])
  
  if msg.payload.decode() == "source":
    print("source")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_S"])
  
  if msg.payload.decode() == "uponeenter":
    print("uponenter")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_UP"])
    time.sleep(.3)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_ENTER"])
    
    
  if msg.payload.decode() == "downoneenter":
    print("downonenter")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_S"])
    time.sleep(.3)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_ENTER"])
  
  if msg.payload.decode() == "uptwoenter":
    print("uptwoenter")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_UP"])
    time.sleep(.2)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_UP"])
    time.sleep(.2)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_ENTER"])
    
    
  if msg.payload.decode() == "downtwoenter":
    print("downtwonter")
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_DOWN"])
    time.sleep(.2)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_DOWN"])
    time.sleep(.2)
    rtn = subprocess.call(["irsend", "SEND_ONCE", "tv", "KEY_ENTER"])
    
client = mqtt.Client()
client.connect("192.168.1.9",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
