#------------------------------ [IMPORT]-----------------------------------
from machine import Pin,Timer, RTC
import time, urequests, network
import dht 
import random
import time
from hcsr04 import HCSR04
import ufirebase as firebase
import os as MOD_OS
import network as MOD_NETWORK
import time as MOD_TIME
from umqtt.simple import MQTTClient
import dht
import ujson
from time import sleep



sensorLum = Pin (4, Pin.IN)
sensorSis = Pin (5, Pin.IN)
led = Pin (2, Pin.OUT)

sensorDis = HCSR04(trigger_pin=18, echo_pin=19, echo_timeout_us=10000)

def conectaWifi(red, password):
    global miRed
    miRed= network.WLAN(network.STA_IF)
    if not miRed.isconnected():
        miRed.active(True)
        miRed.connect(red,password)
        print("Conectando a la red", red +"...")
        timeout = time.time()
        while not miRed.isconnected():
            if(time.ticks_diff(time.time (), timeout)>10):
                return False
    return True 
if conectaWifi("iPhone de uprizing","12345678"):
    print("conexion exitosa!")
    print("Datos de la red (IP/netmask/gw/DNS):",miRed.ifconfig())
#import ntptime
#ntptime.settime()
#--------------------------- [OBJETOS]---------------------------------------
(year, month, day, weekday, hour, minute, second, milisecond) = RTC().datetime()                
#Corrija su Zona Horaria GMT en la variable hour
#Ejemplo: Zona Horaria GMT corregida para Ecuador: GMT-5 = hour-5
RTC().init((year, month, day, weekday, hour-5, minute, second, milisecond))
Hora = ("Hora: {:02d}:{:02d}:{:02d}".format(RTC().datetime()[4], RTC().datetime()[5], RTC().datetime()[6]))
fecha = ("Fecha: {:02d}/{:02d}/{}".format(RTC().datetime()[2], RTC().datetime()[1], RTC().datetime()[0]))
print (Hora)
print (fecha)
while True:
    time.sleep(0.5)
    V = sensorLum.value()
    led.value(V)
    print ("Luminosidad:"+str(V))
    distance = sensorDis.distance_cm()
    print('Distance:', distance, 'cm')
    sleep(1)
    if distance < float(25.0):
        istance = sensorDis.distance_cm()
        Hora = (" {:02d}:{:02d}:{:02d}".format(RTC().datetime()[4], RTC().datetime()[5], RTC().datetime()[6]))
        fecha = (" {:02d}/{:02d}/{}".format(RTC().datetime()[2], RTC().datetime()[1], RTC().datetime()[0]))
        url1="https://maker.ifttt.com/trigger/BotDis/with/key/nLowVPNacdkEqQI27b0IKq1dMTbxJvLIwO5Q4Rw8Zp1?"
        respuesta1=urequests.get(url1+"&value1="+str(istance)+"&value2="+str(Hora)+"&value3="+str(fecha))
        respuesta1.close()
        time.sleep(0.2)
        print("Entro distancia")

    s = sensorSis.value()
    print("Sismo:"+ str(s))

    if  s==1:
        url2="https://maker.ifttt.com/trigger/BotSis/with/key/nLowVPNacdkEqQI27b0IKq1dMTbxJvLIwO5Q4Rw8Zp1?"
        respuesta2=urequests.get(url2+"&value1="+str())
        respuesta2.close()
        time.sleep(0.2)



    
    
        
        