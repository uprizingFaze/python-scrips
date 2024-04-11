from machine import Pin as pin,ADC,I2C
from utime import sleep_ms
from ssd1306 import SSD1306_I2C
import framebuf


sensory1 = ADC(pin(33))   # pines usados el 35,34,33,36, 39 , 32, 
sensorx1 = ADC(pin(32))   # pines usados el 35,34,33,36, 39 , 32, 
sensorx2 = ADC(pin(2))   # pines usados el 35,34,33,36, 39 , 32, 
sensory2 = ADC(pin(4))   # pines usados el 35,34,33,36, 39 , 32, 

boton= pin(25,pin.IN,pin.PULL_UP)
boton2=pin(15,pin.IN,pin.PULL_UP)
boton3=pin(18,pin.IN,pin.PULL_UP)

sensorx1.atten(ADC.ATTN_11DB)   # para calibrar de 0 a 3.6v
sensorx1.width(ADC.WIDTH_12BIT) # establecer resolución
sensory1.atten(ADC.ATTN_11DB)   # para calibrar de 0 a 3.6v
sensory1.width(ADC.WIDTH_12BIT) # establecer resolución

sensorx2.atten(ADC.ATTN_11DB)   # para calibrar de 0 a 3.6v
sensorx2.width(ADC.WIDTH_12BIT) # establecer resolución
sensory2.atten(ADC.ATTN_11DB)   # para calibrar de 0 a 3.6v
sensory2.width(ADC.WIDTH_12BIT) # establecer resolución

ancho = 128
alto = 64
i2c = I2C(0, scl=pin(22), sda=pin(23))
oled = SSD1306_I2C(ancho, alto, i2c)

#marcador
marcador1=0
marcador2=0 

#Pelota
#pelota1=graphics.fill_circle(64,32,2,1)
pelota_x=64
pelota_y=32
m_x=3
m_y=3
max_x = 128
min_x = 0
max_y = 64
min_y = 0

#jugadores
Jugador1_x=8
Jugador1_y=20
Jugador2_x=118
Jugador2_y=20

while True:

    oled.fill(1)

    oled.line(3,1,3,62,0)
    oled.line(125,1,125,62,0)
    oled.line(125,1,3,1,0)
    oled.line(125,62,3,62,0)

    oled.line(42,1,42,10,0)
    oled.line(84,1,84,10,0)
    oled.text(f"{marcador1} P1",31,3,0)
    oled.line(63,1,63,10,0)
    oled.text(f"P2 {marcador2}",64,3,0)
    oled.line(30,1,30,10,0)
    oled.line(96,1,96,10,0)
    oled.line(30,10,96,10,0)   
    oled.rect(min_x,min_y,max_x-min_x,max_y-min_y, 0)
   # oled.vline(63,1,64,1)
    
    oled.line(63,12,63,15,0)
    oled.line(63,18,63,21,0)
    oled.line(63,24,63,27,0)
    oled.line(63,30,63,33,0)
    oled.line(63,36,63,39,0)
    oled.line(63,42,63,45,0)
    oled.line(63,48,63,51,0)
    oled.line(63,54,63,57,0)
    oled.line(63,60,63,62,0)
    
    oled.fill_rect(Jugador1_x,Jugador1_y,2,15,0)
    oled.fill_rect(Jugador2_x,Jugador2_y,2,15,0)
    oled.fill_rect(pelota_x, pelota_y,1,1,0)
    oled.show()
    pelota_x += m_x
    pelota_y += m_y

 
    if pelota_y>4:
        m_y*=-1
    if pelota_y<59:
        m_y*=-1
    #eje x
    if pelota_x>127:
       pelota_x=64
       m_x*=-1
       marcador1+=1
       
    if pelota_x<0:
       pelota_x=64
       m_x*=-1
       marcador2+=1
       
    if ((pelota_x>118 and pelota_x<120)
    and (pelota_y<Jugador2_y+15
    and pelota_y>Jugador2_y-16)):
      m_x*=-1
    if ((pelota_x>6 and pelota_x<9)
    and (pelota_y<Jugador1_y+15
    and pelota_y>Jugador1_y-16)):
      m_x*=-1
    x=sensorx1.read()
    y=sensory1.read()
    x2=sensorx2.read()
    y2=sensory2.read()
    oled.fill(1)

    # paletas 
    if y2>3600:
        Jugador1_y-=3
    elif y2<150:
        Jugador1_y+=3
    if y>3600:
        Jugador2_y-=3
    elif y<150:
        Jugador2_y+=3
        
    if marcador1>7:
        marcador1-=7
    if marcador2>7:
        marcador2-=7

    if marcador1>=7:
        oled.line(3,1,3,62,0)
        oled.line(125,1,125,62,0)
        oled.line(125,1,3,1,0)
        oled.line(125,62,3,62,0)
        oled.text("GANADOR",36, 22,0)
        oled.text("P1", 55, 32,0)
        oled.show()
        oled.fill(1)
        sleep_ms(400)
    if marcador2>=7:
        oled.line(3,1,3,62,0)
        oled.line(125,1,125,62,0)
        oled.line(125,1,3,1,0)
        oled.line(125,62,3,62,0)
        oled.text("GANADOR",36, 22,0)
        oled.text("P2", 55, 32,0)
        oled.show()
        oled.fill(1)
        sleep_ms(400)
    if not boton.value():
        m1.value(0)
        m2.value(0)
    if marcador1>=10:
        m1.value(0)
        m2.value(1)
        sleep_ms(100)
        m1.value(0)
        m2.value(0)