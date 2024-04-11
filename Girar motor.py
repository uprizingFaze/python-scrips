from machine import Pin, PWM
import bluetooth
from BLE import BLEUART
import utime
from utime import sleep as pausa, sleep_ms

m1= Pin (22, Pin.OUT)
m2 = Pin (23, Pin.OUT)
name="La presion"
servo = PWM(Pin(15), freq=50)
print (name, "Conecct")
ble = bluetooth.BLE()
uart = BLEUART (ble, name)


            
def on_rx():
    rx_recibe = uart.read().decode().strip()
    uart.write("Dato:" + str(rx_recibe))
    print(rx_recibe)

 
    if rx_recibe == "!B516":
        
        servo.duty_u16(3000)
        pausa(2)
        m1.value(1)
        m2.value(0)
        
    
    if rx_recibe == "!B507":
        
        servo.duty_u16(1500)
        
        m1.value(0)
        m2.value(0)
        
    if rx_recibe == "!B813":
        m1.value(0)
        m2.value(1)
        
        servo.duty_u16(3000)
        print("motor 1")
    
    if rx_recibe == "!B804":
        
        servo.duty_u16(1500)
        
        m1.value(0)
        m2.value(0)
        print("servo")
        
        
uart.irq(handler= on_rx)
