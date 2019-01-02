import requests
e =requests.get('https://api.thingspeak.com/apps/thinghttp/send_request?api_key=0443YZNWB5PY1Q7K')
print (e.text)
#percentstart = e.text.find("--q")
#percentend = e.text.find("/span")
                      
#eprice = e.text[percentstart+5:percentend-1]
#print (eprice)
#print (idx)


