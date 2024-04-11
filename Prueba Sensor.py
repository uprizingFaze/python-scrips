# Complete project details at https://RandomNerdTutorials.com

from machine import Pin
from time import sleep
import dht 

#sensor = dht.DHT22(Pin(13))
sensor = dht.DHT11(Pin(13))

while True:
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    print(temp)
    print(temp_f)
    print(hum)
  except OSError as e:
    print('Failed to read sensor.')