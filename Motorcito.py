from machine import Pin, PWM
import bluetooth
from BLE import BLEUART
import utime
name= "La presion (ESP)"
ble = bluetooth.BLE()
uart = BLEUART(ble, name)
servo = PWM(Pin(13), freq=50)
print ("Nicolas")

def mapear (valor_sensor, minimo_entrada, maximo_entrada, minimo_salida, maximo_salida):
    valor_mapeado = (valor_sensor - minimo_entrada) * (maximo_salida - minimo_salida) / (maximo_entrada-minimo_entrada)+minimo_salida 
    return valor_mapeado
def on_rx():
    rx_recibe = uart.read().decode().strip()
    dato=float(rx_recibe)
    if dato>=0 and dato<=180:
        uart.write("angulo:" + str(dato)+ "\n")
        print("angulo"+ str(dato)+ "\n")
        mi=int(mapear(dato,0,180,1150,8190))
        print (mi)
        
        servo.duty_u16(mi)
    else:
        uart.write("el valor no aplica")
        print("el valor no aplica")
uart.irq(handler=on_rx)