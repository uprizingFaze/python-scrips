from machine import Pin, PWM
import time, urequests, network
import dht 
import random
import time
import ufirebase as firebase
import os as MOD_OS
import network as MOD_NETWORK
import time as MOD_TIME

servo = PWM(Pin(21), freq=50)

sensor = dht.DHT11(Pin(13))
sismo = Pin(2, Pin.IN)


def mapear (valor_sensor, minimo_entrada, maximo_entrada, minimo_salida, maximo_salida):
    valor_mapeado = (valor_sensor - minimo_entrada) * (maximo_salida - minimo_salida) / (maximo_entrada - minimo_entrada)+minimo_salida 
    return valor_mapeado

servo.duty_u16(2000)

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
   
#########################

    while True:
        time.sleep(2)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        
        print("T={:02d} °C, H={:02d} %".format (temp,hum))

        V = sismo.value()
        print (V)
        time.sleep(0.2) 
        if V > 0:

            url1="https://maker.ifttt.com/trigger/BotSis/with/key/nLowVPNacdkEqQI27b0IKq1dMTbxJvLIwO5Q4Rw8Zp1?"
            respuesta1=urequests.get(url1+"&value1="+str(V))
            respuesta1.close()

        time.sleep(0.2)
        if temp > 35:
            url2="https://maker.ifttt.com/trigger/BotDis/with/key/nLowVPNacdkEqQI27b0IKq1dMTbxJvLIwO5Q4Rw8Zp1?"
            respuesta3=urequests.get(url2+"&value1="+str(temp))
            respuesta3.close()

        time.sleep(0.2)
        if hum > 70:
            url3="https://maker.ifttt.com/trigger/BotHum/with/key/nLowVPNacdkEqQI27b0IKq1dMTbxJvLIwO5Q4Rw8Zp1?"
            respuesta3=urequests.get(url3+"&value1="+str(hum))
            respuesta3.close()
        
        firebase.setURL("https://casaseguridad-dabc2-default-rtdb.firebaseio.com/")
        firebase.put("Proyecto/Final", "", bg =0)
        y=0
        firebase.get("Proyecto/Final", "x")
        print (f"Final: {str(firebase.x)}")
        y=(firebase.x)
        time.sleep(0.2)
        print ("Variable:" +y)

        print(type(y))
        dato = float (y)
        
        print(type(dato))
               
        print (dato)
        if dato >= 0 and dato <= 180:           
            time.sleep(0.2)    
            print("angulo "+ str(dato))
            mi=int(mapear(dato,0,180,1150,8190))
            print(type(mi))
            print (mi)        
            servo.duty_u16(mi)
        else:            
            print("el valor no aplica")        
       # url4="https://api.thingspeak.com/update?api_key=W32QACQCVOVJD3JN"
       # respuesta2=urequests.get(url4+"&field1="+str(temp)+"&field2="+str(hum))
       # respuesta2.close()       
else:
    print("Imposible conectar")
    miRed.active(False)