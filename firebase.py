#------------------------------ [IMPORT]------------------------------------
import network
import time
from machine import Pin,Timer
import dht
import ujson
from umqtt.simple import MQTTClient 
import os as MOD_OS
import network as MOD_NETWORK
import time as MOD_TIME

red = Pin(15, Pin.OUT)
green = Pin(2, Pin.OUT)
blue = Pin(4, Pin.OUT)

x=0
#----------------------[ CONECTAR WIFI ]---------------------------------------------------------#
print("Conectando al WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Redmi Note 9S', 'rockstar') 
while not sta_if.isconnected():
  print(".", end="")
  time.sleep(0.1)
print(" Connected!")
#------------p-----


import ufirebase as firebase
firebase.setURL("https://appinventorarq-default-rtdb.firebaseio.com/")
firebase.put("LedRGB/color/RGB", "", bg =0)
while True:
    firebase.get("LedRGB/RGB", "x")
    print (f"COLOR: {str(firebase.x)}")

   # firebase.ger()
   # print ("hall: "+str(firebase.var2))
   # time.sleep(1)
    y=float(firebase.x)
   # firebase.get()
   # print()
    time.sleep(0.2)
    
    
    print ("Variable:" +y)

    #Amarillo  1

    if y == str(1):
          green.value(1)
          red.value(1)
          blue.value(0)
          print("Amarillo")

    #Rojo  2
    if y ==str(2):
          red.value(1)
          green.value(0)
          blue.value(0)
          print("Rojo")


    #morado 3
    if  y == str(3):
          blue.value(1)
          red.value(1)
          green.value(0)
          print ("Morado")

    #Verde 4
    if y ==str(4):
          green.value(1)
          blue.value(0)
          red.value(0)
          print("Verde")


    # Cian 5
    if y ==str(5):
          green.value(1)
          red.value(1)
          blue.value(1)
          print("Cian")


    # azul 6

    if y ==str(6):
          blue.value(1)
          red.value(0)
          green.value(0)
          print  ("Azul")

    



