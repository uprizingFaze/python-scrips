#--------------------------- [Modulos y Clases]---------------------------------------
import network, time, urequests
from machine import Pin, ADC, PWM
from utelegram import Bot
import utime

#--------------------------- [Token de telegram ]---------------------------------------

TOKEN = '5762374722:AAFd3FNlq4YV3FBbmAhyfc918U5s6APZpE0'
#--------------------------- [OBJETOS]---------------------------------------

bot = Bot(TOKEN)
led  = Pin(2, Pin.OUT)

#----------------------[ CONECTAR WIFI ]---------------------------------------------------------#

def conectaWifi (red, password):
      global miRed
      miRed = network.WLAN(network.STA_IF)     
      if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
      return True

#------------------------------------[BOT]---------------------------------------------------------------------#

if conectaWifi ("iPhone de uprizing", "12345678"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
    print("ok")

    @bot.add_message_handler("Ok")
    def help(update):
        update.reply(" Menu: Prender : On   Apagar : Off ")

    @bot.add_message_handler("On")
    def help(update):
        led.value(1)
        update.reply("Encendido \U0001F600")

    @bot.add_message_handler("Off")
    def help(update):
        led.value(0)
        update.reply("apagado \U0001F636")

    


    bot.start_loop()

else:
    print ("Imposible conectar")
    miRed.active (False)