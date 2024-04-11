#!
#------------------------------ [IMPORT]------------------------------------

from machine import Pin, PWM, RTC, Timer, I2C
import time, urequests, network
import dht 
import random
import time
from hcsr04 import HCSR04
import ufirebase as firebase
import os as MOD_OS
import network as MOD_NETWORK
import time as MOD_TIME
import ntptime
from umqtt.simple import MQTTClient
import dht
import ujson
from time import sleep
from ssd1306 import SSD1306_I2C
import framebuf
import ntptime


def mapear (valor_sensor, minimo_entrada, maximo_entrada, minimo_salida, maximo_salida):
    valor_mapeado = (valor_sensor - minimo_entrada) * (maximo_salida - minimo_salida) / (maximo_entrada - minimo_entrada)+minimo_salida 
    return valor_mapeado

sensorDis = HCSR04(trigger_pin=25, echo_pin=33, echo_timeout_us=10000)


Fot = Pin(13, Pin.IN)
led = Pin (14, Pin.OUT)

sismo = Pin(12, Pin.IN)

red = Pin(15, Pin.OUT)
green = Pin(4, Pin.OUT)
blue = Pin(2, Pin.OUT)


time.sleep(1)
#----------------------[ FUNCION Hora ]---------------------------------------------------------#
(year, month, day, weekday, hour, minute, second, milisecond) = RTC().datetime()                
#Corrija su Zona Horaria GMT en la variable hour
#Ejemplo: Zona Horaria GMT corregida para Ecuador: GMT-5 = hour-5
RTC().init((year, month, day, weekday, hour-5, minute, second, milisecond))
Hora = ("Hora: {:02d}:{:02d}:{:02d}".format(RTC().datetime()[4], RTC().datetime()[5], RTC().datetime()[6]))
fecha = ("Fecha: {:02d}/{:02d}/{}".format(RTC().datetime()[2], RTC().datetime()[1], RTC().datetime()[0]))

print (Hora)
print (fecha)
################## ^^^^ ##############

distance = sensorDis.distance_cm()
print('Distance:', distance, 'cm')

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


#dht = dht.DHT11(Pin(15))


################## ^^^^ ################################ ^^^^ ################################ ^^^^ ################################ ^^^^ ##############
time.sleep(1)
#--------------------------- [OBJETOS]---------------------------------------
temporiza=Timer(0)                     # se instancia un objeto de la clase Timer
prev_weather=0

# MQTT Server Parameters
MQTT_CLIENT_ID = "clientId-1qrJjnLQf12p"
MQTT_BROKER    = "broker.mqttdashboard.com"
MQTT_USER      = ""
MQTT_PASSWORD  = ""

#[------------------- Servos ----------------------------]
topic_sub1      = 'Serv/1'
topic_sub2      = 'Serv/2'
topic_sub3      = 'Serv/3'
topic_sub4      = 'Serv/4'
time.sleep(1)
def sub_cb(topic, msg):
    print(f"llego el topic: {topic} con el valor {msg}")

    if topic== b'Serv/1':
        fun=int (msg.decode())
        print(f'Serv/1:{fun}')
        print("angulo "+ str(fun))
        mi=int(mapear(fun,0,180,1150,8190))
        if fun == 1:
            A= 180
            mi=int(mapear(A,0,180,1150,8190))
            print(type(mi))
            print (mi)        
            servo1.duty_u16(mi)
        else:
            A = 90
            mi=int(mapear(A,0,180,1150,8190))
            print(type(mi))
            print (mi)        
            servo1.duty_u16(mi)


            
  

#----------------------[ CONECTAR BROKER ]---------------------------------------------------------#
time.sleep(1)
print("Connecting to MQTT server... ", end="")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic_pub1)
client.subscribe(topic_pub2)
client.subscribe(topic_pub3)
client.subscribe(topic_pub4)
client.subscribe(topic_pub5)
#client.subscribe(topic_sub1)
#client.subscribe(topic_sub2)
#client.subscribe(topic_sub3)
#client.subscribe(topic_sub4)
#client.subscribe(topic_sub5)
#client.subscribe(topic_sub6)
#client.subscribe(topic_sub7)
#client.subscribe(topic_sub8)
#client.subscribe(topic_sub9)

print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub1))
print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub2))
print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub3))
#print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub4))
#print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub5))
#print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub6))
#print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub7))
#print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub8))
#print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub9))

print("Connected!")
prev_weather = ""

time.sleep(1)



while True:

    print ("esperando(Bucle)")
    

    client.wait_msg()


################## ^^^^ ################################ ^^^^ ################################ ^^^^ ################################ ^^^^ ##############
