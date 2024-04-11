from machine import Pin, ADC, I2C
import network
import time
import json
import urequests
from ssd1306 import SSD1306_I2C
import framebuf

############################## OLED  ########################################
ancho=128
alto=64
i2c = I2C(1, scl=Pin(22), sda=Pin(23)) 
oled = SSD1306_I2C(ancho, alto, i2c)
##############################  ^^^^ ########################################

def Abrir_Icono(ruta_icono):
    doc = open(ruta_icono,"rb")
    doc.readline()
    xy= doc.readline()
    x = int(xy.split()[0])
    y = int(xy.split()[1])
    
    icono = bytearray(doc.read())
    doc.close()
    return framebuf.FrameBuffer(icono, x, y, framebuf.MONO_HLSB)

oled.text("12", 50,10, 1)
oled.text("=", 40,10, 1)
oled.blit(Abrir_Icono("Imagenes/ther24.pbm"), 15, 2)

oled.blit(Abrir_Icono("Imagenes/humidity.pbm"), 15, 40)
oled.text("12", 50,50, 1)
oled.text("=", 40,50, 1)

oled.show()