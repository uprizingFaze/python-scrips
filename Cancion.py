from machine import Pin, ADC, PWM
from utime import sleep_ms

def mapear(valor_sensor, minimo_entrada, maximo_entrada, minimo_salida, maximo_salida):
  valor_mapeado = (valor_sensor - minimo_entrada) * (maximo_salida - minimo_salida) / (maximo_entrada - minimo_entrada) + minimo_salida
  return valor_mapeado
#--------------------------- [OBJETOS]---------------------------------------
bombillor  = PWM(Pin (4),1000)
bombillog  = PWM(Pin (15),1000)
bombillob  = PWM(Pin (2),1000)
potr = ADC(Pin(35))
potg = ADC(Pin(32))
potb = ADC(Pin(33))

  


while True:
  print(f"rojo:{potr.read()}\t verde:{potg.read()} \t azul:{potb.read()}")
  bombillor.duty( int (potr.read()/4))
  bombillog.duty( int (potg.read()/4))
  bombillob.duty( int (potb.read()/4))
  # bombillo.duty( int (pot.read/4))
  # bombillo.duty_ns( pot.read()*16)
  sleep_ms(30)