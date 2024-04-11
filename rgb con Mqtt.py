#------------------------------ [IMPORT]------------------------------------
from machine import Pin, PWM, RTC, Timer
import time, urequests, network
import dht 
import random
import time
import ufirebase as firebase
import os as MOD_OS
import network as MOD_NETWORK
import time as MOD_TIME
import ntptime
from umqtt.simple import MQTTClient
import dht
import ujson

servo = PWM(Pin(21), freq=50)

sensor = dht.DHT11(Pin(13))
sismo = Pin(2, Pin.IN)


def mapear (valor_sensor, minimo_entrada, maximo_entrada, minimo_salida, maximo_salida):
    valor_mapeado = (valor_sensor - minimo_entrada) * (maximo_salida - minimo_salida) / (maximo_entrada - minimo_entrada)+minimo_salida 
    return valor_mapeado
#--------------------------- [OBJETOS]---------------------------------------
temporiza=Timer(0)                     # se instancia un objeto de la clase Timer
prev_weather=0

# MQTT Server Parameters
MQTT_CLIENT_ID = "clientId-1qrJjnLQfp"
MQTT_BROKER    = "broker.mqttdashboard.com"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
#topic_pub     = "testt/1"
topic_sub1      = 'Nicolas/temp'
topic_sub2      = 'Nicolas/hum'
topic_sub3      = 'Nicolas/3000'
topic_sub4      = 'Nicolas/Amarillo'
topic_sub5      = 'Nicolas/Rojo'
topic_sub6      = 'Nicolas/Morado'
topic_sub7      = 'Nicolas/Verde'
topic_sub8      = 'Nicolas/Cian'
topic_sub9      = 'Nicolas/Azul'


#topic_pub2    ="javier/temperatura"
sensor = dht.DHT22(Pin(15))
#----------------------[ CONECTAR WIFI ]---------------------------------------------------------#
print("Conectando al WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('ALFONSO_2G-Etb', '1000705888')
while not sta_if.isconnected():
  print(".", end="")
  time.sleep(0.1)
print(" Connected!")
#----------------------[ FUNCION Hora ]---------------------------------------------------------#

# OBTENCIÓN DESDE INTERNET DE NTP - NETWORK TIME PROTOCOL (pool.ntp.org)

ntptime.settime()
#____________________________________________________________________________________________________________
# SINCRONIZACION DEL RELOJ INTERNO E IMPRESION DE FECHA Y HORA
(year, month, day, weekday, hour, minute, second, milisecond) = RTC().datetime()                
#Corrija su Zona Horaria GMT en la variable hour
#Ejemplo: Zona Horaria GMT corregida para Ecuador: GMT-5 = hour-5
RTC().init((year, month, day, weekday, hour-5, minute, second, milisecond))
print ("Fecha: {:02d}/{:02d}/{}".format(RTC().datetime()[2], RTC().datetime()[1], RTC().datetime()[0])) 
print ("Hora: {:02d}:{:02d}:{:02d}".format(RTC().datetime()[4], RTC().datetime()[5], RTC().datetime()[6]))



#----------------------[ FUNCION RECEPCION EN EL SUB ]---------------------------------------------------------#
def sub_cb(topic, msg):
  print(f"llego el topic: {topic} con el valor {msg}")
  if topic== b'Nicolas/1000':
    fun=int (msg.decode())
    print(f'Luz red :{fun}')
    red.value(fun)
  if topic== b'Nicolas/2000':
    fun=int (msg.decode())
    print(f'Luz green :{fun}')
    green.value(fun)
  if topic== b'Nicolas/3000':
    fun=int (msg.decode())
    print(f'Luz blue :{fun}')
    blue.value(fun)
    
  
#----------------------[ Ifs ]---------------------------------------------------------#

  if topic== b'Nicolas/Amarillo':
        fun=int (msg.decode())
    print(f'Amarillo:{fun}')
    green.value(fun)
    red.value(fun)
    blue.value(0)

  if topic== b'Nicolas/Rojo':
    fun=int (msg.decode())
    print(f'Rojo:{fun}')
    red.value(fun)
    green.value(0)
    blue.value(0)


  if topic== b'Nicolas/Morado':
      fun=int (msg.decode())
      print(f'Morado:{fun}')
      blue.value(fun)
      red.value(fun)
      green.value(0)

  if topic== b'Nicolas/Verde':
    fun=int (msg.decode())
    print(f'Verde:{fun}')
    green.value(fun)
    blue.value(0)
    red.value(0)

  if topic== b'Nicolas/Cian':
    fun=int (msg.decode())
    print(f'Cian:{fun}')
    green.value(fun)
    red.value(fun)
    blue.value(fun)

  if topic== b'Nicolas/Azul':
    fun=int (msg.decode())
    print(f'Azul:{fun}')
    blue.value(fun)
    red.value(0)
    green.value(0)

#----------------------[ CONECTAR BROKER ]---------------------------------------------------------#
print("Connecting to MQTT server... ", end="")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic_sub1)
client.subscribe(topic_sub2)
client.subscribe(topic_sub3)
client.subscribe(topic_sub4)
client.subscribe(topic_sub5)
client.subscribe(topic_sub6)
client.subscribe(topic_sub7)
client.subscribe(topic_sub8)
client.subscribe(topic_sub9)


print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub1))
print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub2))
print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub3))
print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub4))
print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub5))
print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub6))
print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub7))
print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub8))
print('Connected to %s MQTT broker, subscribed to %s topic' % (MQTT_BROKER, topic_sub9))

print("Connected!")
prev_weather = ""
#----------------------[ TIMER INTERUPCION ]---------------------------------------------------------#
def desborde (Timer):
      global prev_weather
      sensor.measure()     #entrega error cuando el sensor esta desconectado
      message = ujson.dumps({"temp": sensor.temperature(),"humidity": sensor.humidity(),})
      tempe=sensor.temperature()
      if message != prev_weather:
        print("valor publicado en el topic {}: {}".format(topic_pub, message))
        client.publish(topic_pub, message)
        prev_weather = message
        client.publish(topic_pub2, str(sensor.temperature()))
        print("valor publicado en el topic {}: {}".format(topic_pub2, tempe))
#----------------------[ CICLO INFINITO ]---------------------------------------------------------#
while True:
  print ("esperando")
  client.wait_msg()