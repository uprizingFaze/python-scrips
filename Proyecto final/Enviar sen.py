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


sensorDis = HCSR04(trigger_pin=25, echo_pin=33, echo_timeout_us=10000)


Fot = Pin(13, Pin.IN)
led = Pin (14, Pin.OUT)

sismo = Pin(12, Pin.IN)




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
topic_pub1     = "Nicolas/Hora"
topic_pub2    = "Nicolas/Temp"
topic_pub3    = "Nicolas/Serv1"
topic_pub4    = "Nicolas/Serv2"
topic_pub5    = "Nicolas/Dis"
topic_sub1      = 'Nicolas/1'
topic_sub2      = 'Nicolas/2'
topic_sub3      = 'Nicolas/3'
topic_sub4      = 'Nicolas/4'
topic_sub5      = 'Nicolas/5'

time.sleep(1)
def sub_cb(topic, msg):
    print(f"llego el topic: {topic} con el valor {msg}")
    if topic== b'Nicolas/3':
        fun=int (msg.decode())
        print(f'Nicolas/3:{fun}')
        if fun == 0:
            print("Cerrado")
            red.value(1)
            green.value(0)
            blue.value(0)
            
  
            
        else:
            print("Abierto")
            red.value(0)
            green.value(1)
            blue.value(0)
    print(Fot.value())
    if  Fot.value == 0:
        led.value(1)
    else:
        led.value(0)
            
#----------------------[ CONECTAR BROKER ]---------------------------------------------------------#
time.sleep(1)
print("Connecting to MQTT server... ", end="")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
client.set_callback(sub_cb)
client.connect()

client.subscribe(topic_sub1)
client.subscribe(topic_sub2)
client.subscribe(topic_sub3)


print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub1))
print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub2))
print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub3))

print("Connected!")
prev_weather = ""

time.sleep(1)



while True:

    print ("esperando(Bucle)")
    

    client.wait_msg()


################## ^^^^ ################################ ^^^^ ################################ ^^^^ ################################ ^^^^ ##############










#while True:
#    dht.measure()
#    F = Fot.value()
#    print (F)
#    time.sleep(0.2)
#    #led.value(V)
#    S = sismo.value()
#    print (S)
#    time.sleep(0.2)
#
#    print('Temperature = %.2f' % dht.temperature())
#    time.sleep(3)
