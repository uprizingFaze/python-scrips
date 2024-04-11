from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausa
puerto=[15,2,4,16,17,18,19,21,3,1]
x=[]
btr=pin(27, pin.IN)
bty=pin(14, pin.IN)
btb=pin(12, pin.IN)
btg=pin(13, pin.IN)
for i in puerto:
    x.append(pin(i,pin.OUT))
print (x)
def primero():
    for i in x:
        for j in range (15):
            i. value(not  i.value())
        pausa(50)
def segundo():
    for i in reversed (x):
        for j in range (15):
            i. value(not i.value())
        pausa(50)
def tercero():
    for i in x:
        for j in range (15):
            i. value(i.value())
        pausa(50)
def cuarto():
    for i in x:
        for j in reversed (15):
            i. value(i.value())
        pausa(50)
        
while (True):
    
    if (btr.value()==0):
        primero()
        
    else:
       
       if (bty.value()==0):
           segundo()
         
