#------------------------------ [IMPORT]------------------------------------

from machine import Pin, PWM, RTC, Timer
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
dato =0
temporiza=Timer(0)                     # se instancia un objeto de la clase Timer
prev_weather=0
V=0
servo1 = PWM(Pin(13), freq=50)
servo2 = PWM(Pin(12), freq=50)
servo3 = PWM(Pin(14), freq=50)
servo4 = PWM(Pin(27), freq=50)

red = Pin(15, Pin.OUT)
green = Pin(4, Pin.OUT)
blue = Pin(2, Pin.OUT)


sensor = 18
sensorDis = HCSR04(trigger_pin=18, echo_pin=19, echo_timeout_us=10000)
#--------------------------- [Wifi]---------------------------------------#
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
#--------------------------- [Mapeado]---------------------------------------#
def mapear (valor_sensor, minimo_entrada, maximo_entrada, minimo_salida, maximo_salida):
    valor_mapeado = (valor_sensor - minimo_entrada) * (maximo_salida - minimo_salida) / (maximo_entrada - minimo_entrada)+minimo_salida 
    return valor_mapeado
#--------------------------- [OBJETOS]---------------------------------------
temporiza=Timer(0)                     # se instancia un objeto de la clase Timer
prev_weather=0
MQTT_CLIENT_ID = "clientId-1qrJjnLQfp"
MQTT_BROKER    = "broker.mqttdashboard.com"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
topic_sub1      = 'Serv/1'
topic_sub2      = 'Serv/2'
topic_sub3      = 'Serv/3'
topic_sub4      = 'Serv/4'
#----------------------[ FUNCION Hora ]---------------------------------------------------------#
(year, month, day, weekday, hour, minute, second, milisecond) = RTC().datetime()                
RTC().init((year, month, day, weekday, hour-5, minute, second, milisecond))
print ("Fecha: {:02d}/{:02d}/{}".format(RTC().datetime()[2], RTC().datetime()[1], RTC().datetime()[0])) 
print ("Hora: {:02d}:{:02d}:{:02d}".format(RTC().datetime()[4], RTC().datetime()[5], RTC().datetime()[6]))
message = ("Hora: {:02d}:{:02d}:{:02d}".format(RTC().datetime()[4], RTC().datetime()[5], RTC().datetime()[6]))
#----------------------[ FUNCION RECEPCION EN EL SUB ]---------------------------------------------------------#
def sub_cb(topic, msg):
    print(f"llego el topic: {topic} con el valor {msg}")
#----------------------[Servo 1]----------------------------------#
    if topic== b'Serv/1':
        fun=int (msg.decode())
        print(f'Serv/1:{fun}')
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
#----------------------[Servo 2]----------------------------------#
    if topic== b'Serv/2' :
        fun=int (msg.decode())
        print(f'Serv/2:{fun}')
        print("valor publicado en el topic {}: {}".format(topic_sub2, fun))
        if fun == 1:
            A= 180
            mi=int(mapear(A,0,180,1150,8190))
            print(type(mi))
            print (mi)        
            servo2.duty_u16(mi)
            green.value(1)
            red.value(0)
            blue.value(0)
        else:
            A = 90
            mi=int(mapear(A,0,180,1150,8190))
            print(type(mi))
            print (mi)        
            servo2.duty_u16(mi)
            green.value(0)
            red.value(1)
            blue.value(0)
#----------------------[Servo 3]----------------------------------#
    if topic== b'Serv/3' :
        fun=int (msg.decode())
        print(f'Serv/3:{fun}')
        if fun == 1:
            A= 180
            mi=int(mapear(A,0,180,1150,8190))
            print(type(mi))
            print (mi)        
            servo3.duty_u16(mi)
        else:
            A = 90
            mi=int(mapear(A,0,180,1150,8190))
            print(type(mi))
            print (mi)        
            servo3.duty_u16(mi)
#----------------------[Servo 4]----------------------------------#
    if topic== b'Serv/4' :
        fun=int (msg.decode())
        print(f'Serv/4:{fun}')
        if fun == 1:
            A= 180
            mi=int(mapear(A,0,180,1150,8190))
            print(type(mi))
            print (mi)        
            servo4.duty_u16(mi)
        else:
            A = 90
            mi=int(mapear(A,0,180,1150,8190))
            print(type(mi))
            print (mi)        
            servo4.duty_u16(mi)

    if topic == b'Led/1' or V == 0:
        fun=int (msg.decode())
        print(f'Led/1:{fun}')
        led.value


#----------------------[ CONECTAR BROKER ]---------------------------------------------------------#
print("Connecting to MQTT server... ", end="")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic_sub1)
client.subscribe(topic_sub2)
client.subscribe(topic_sub3)
client.subscribe(topic_sub4)

print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub1))
print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub2))
print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub3))
print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub3))

print("Connected!")
prev_weather = ""
#----------------------[ TIMER INTERUPCION ]---------------------------------------------------------#

#----------------------[ CICLO INFINITO ]---------------------------------------------------------#
while True:
    print ("esperando(Bucle)")  
    client.wait_msg()




    if distance < float(25.0):
        istance = sensorDis.distance_cm()
        Hora = (": {:02d}:{:02d}:{:02d}".format(RTC().datetime()[4], RTC().datetime()[5], RTC().datetime()[6]))
        fecha = (": {:02d}/{:02d}/{}".format(RTC().datetime()[2], RTC().datetime()[1], RTC().datetime()[0]))
        url1="https://maker.ifttt.com/trigger/BotDis/with/key/nLowVPNacdkEqQI27b0IKq1dMTbxJvLIwO5Q4Rw8Zp1?"
        respuesta1=urequests.get(url1+"&value1="+str(istance)+"&value2="+str(Hora)+"&value3="+str(fecha))
        respuesta1.close()
        time.sleep(0.2)
        print("Entro distancia")