from machine import Pin
import time, urequests, network
import dht 
import random
import time
sensor = dht.DHT11(Pin(13))


def conectaWifi(red,password):
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
if conectaWifi('iPhone de uprizing', '12345678'):
    print("conexion exitosa!")
    print("Datos de la red (IP/netmask/gw/DNS):",miRed.ifconfig())
   
    
     
    while True:
        sleep(3)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        temp_f = temp * (9/5) + 32.0
        #temp=random.randint(0,100)
        #hum=random.randint(0,100)
        print("T={:02d} °C, H={:02d} %".format (temp,hum))

        url1="https://maker.ifttt.com/trigger/Bott/with/key/nLowVPNacdkEqQI27b0IKq1dMTbxJvLIwO5Q4Rw8Zp1?"
        respuesta1=urequests.get(url1+"&value1="+str(temp)+"&value2="+str(hum))
        respuesta1.close()

        time.sleep(0.5)

        url2="https://api.thingspeak.com/update?api_key=W32QACQCVOVJD3JN"
        respuesta2=urequests.get(url2+"&field1="+str(temp)+"&field2="+str(hum))
        respuesta2.close()

        
else:
    print("Imposible conectar")        
    miRed.active(False)