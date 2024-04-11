#------------------------------ [IMPORT]------------------------------------

import time
from machine import Pin


sismo = Pin(5, Pin.IN)

while True:
    V = sismo.value()
    print (V)
    time.sleep(0.2)
    V = sismo.value()
    sismo.value(V)
