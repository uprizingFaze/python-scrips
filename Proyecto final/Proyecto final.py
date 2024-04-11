#------------------------------ [IMPORT]------------------------------------
import network
import time
from machine import Pin,Timer
import dht
import ujson
from umqtt.simple import MQTTClient
#--------------------------- [OBJETOS]---------------------------------------
temporiza=Timer(0)                     # se instancia un objeto de la clase Timer
prev_weather=0

red = Pin(15, Pin.OUT)
green = Pin(2, Pin.OUT)
blue = Pin(4, Pin.OUT)

# MQTT Server Parameters
MQTT_CLIENT_ID = "clientId-1qrJjnLQfp"
MQTT_BROKER    = "broker.mqttdashboard.com"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
#topic_pub     = "testt/1"
topic_sub1      = 'Nicolas/1000'
topic_sub2      = 'Nicolas/2000'
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

#----------------------[ CICLO INFINITO ]---------------------------------------------------------#
while True:
  print ("esperando")
  client.wait_msg()