from machine import Pin, PWM
import bluetooth
from BLE import BLEUART
import utime
led_b = Pin(2, Pin.OUT)
m1= Pin (12, Pin.OUT)
m2 = Pin (13, Pin.OUT)
name="Mac"
servo = PWM(Pin(2), freq=50)
print (name, "Lol")
ble = bluetooth.BLE()
uart = BLEUART (ble, name)


            
def on_rx():
    rx_recibe = uart.read().decode().strip()
    uart.write("Dato:" + str(rx_recibe))
    print(rx_recibe)
 
        
        
    if rx_recibe == "!B516":
        
        servo.duty_u16(3000)
        print("servo")
    
    if rx_recibe == "!B507":
        
        servo.duty_u16(3000)
        
        
    
    if rx_recibe == "!B813":
      
        servo.duty_u16(1500)
       
    if rx_recibe == "!B804":
      
        servo.duty_u16(1500)
        
        
        
        
        
uart.irq(handler= on_rx)


    
    
    

