from machine import Pin
import time, urequests,network
from dht import DHT11 
import random
import time
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
if conectaWifi("ALFONSO_5G-Etb","1000705888"):
    print("conexion exitosa!")
    print("Datos de la red (IP/netmask/gw/DNS):",miRed.ifconfig())
    url="https://api.thingspeak.com/update?api_key=9VTPSQYZ73S03QZY"
     
    while True:
        time.sleep(2)
        #sensorDHT.measure()
        #temp=sensorDHT.temperature()
        #hum=sensorDHT.humanidity()
        temp=random.randint(0,100)
        hum=random.randint(0,100)
        print("T={:02d} °C, H={:02d} %".format (temp,hum))
        respuesta=urequests.get(url+"&field1="+str(temp)+"&field2="+str(hum))
        print(respuesta.text)
        print(respuesta.status_code)
        respuesta.close()
else:
    print("Imposible conectar")        
    miRed.active(False)
