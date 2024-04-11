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
i2c = I2C(0, scl=Pin(22), sda=Pin(23)) 
oled = SSD1306_I2C(ancho, alto, i2c)
##############################  ^^^^ ########################################

################## ICONOS ############
def Abrir_Icono(ruta_icono):
    doc = open(ruta_icono,"rb")
    doc.readline()
    xy= doc.readline()
    x = int(xy.split()[0])
    y = int(xy.split()[1])
    
    icono = bytearray(doc.read())
    doc.close()
    return framebuf.FrameBuffer(icono, x, y, framebuf.MONO_HLSB)

################## ^^^^ ##############
 
print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('iPhone de uprizing', '12345678')

while not sta_if.isconnected():
  print(".", end="")
  time.sleep(0.1)
print(" Connected!")
while True:
  consulta=urequests.get("https://api.thingspeak.com/channels/1914085/feeds.json?results=2")
  datos=consulta.json()
  temp=datos["feeds"][1]["field1"]
  hum=datos["feeds"][1]["field2"] 
  fecha=datos["feeds"][1]["created_at"]
  Data=datos["feeds"][1]["entry_id"]
  print ("la temperatura es",temp)
  print ("la humedad es",hum)
  print  ("Fecha ", fecha)
  print ("Dato: ", Data)
  Dts= str(Data)
  #################### OLED ##############################
  oled.fill(0)
  oled.text(temp, 50,10, 1)
  oled.text("=", 40,10, 1)
  oled.blit(Abrir_Icono("Imagenes/celsius.pbm"), 15, 2)

  oled.blit(Abrir_Icono("Imagenes/humidity.pbm"), 15, 40)
  oled.text(hum, 50,50, 1)
  oled.text("=", 40,50, 1)

  oled.text("Act #:", 30,30,1)
  oled.text(Dts, 78,30,1)

  oled.show()
  ################## ^^^^^^^ ##############################
  time.sleep(1)



