from machine import Pin
import utime

m1 = Pin(12,Pin.OUT)
m2 = Pin(13,Pin.OUT)

while True:
    m1.value(1)
    m2.value(0)
    utime.sleep(2)