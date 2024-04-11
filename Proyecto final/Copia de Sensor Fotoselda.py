
import time
from machine import Pin,Timer


Fot = Pin(4, Pin.IN)
led = Pin (2, Pin.OUT)

while True:
    V = Fot.value()
    print (V)
    time.sleep(0.2)
    led.value(V)
