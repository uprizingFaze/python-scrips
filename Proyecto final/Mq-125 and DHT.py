import time
import dht
from machine import Pin
from MQ135 import MQ135


# setup
mq135 = MQ135(Pin(15)) # analog PIN 0
sensor = dht.DHT11(Pin(13))

# loop
while True:
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
    
        rzero = mq135.get_rzero()
        corrected_rzero = mq135.get_corrected_rzero(temperature, humidity)
        resistance = mq135.get_resistance()
        ppm = mq135.get_ppm()
        corrected_ppm = mq135.get_corrected_ppm(temperature, humidity)

        print("DHT11 Temperature: " + str(temperature) +"\t Humidity: "+ str(humidity))
        print("MQ135 RZero: " + str(rzero) +"\t Corrected RZero: "+ str(corrected_rzero)+
              "\t Resistance: "+ str(resistance) +"\t PPM: "+str(ppm)+
              "\t Corrected PPM: "+str(corrected_ppm)+"ppm")
        time.sleep(1)
    except OSError as e:
        print('Failed to read sensor.')