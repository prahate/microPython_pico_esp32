from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)
button = Pin(0, Pin.IN, Pin.PULL_UP)

def ledON():
    led.value(1)

def ledOFF():
    led.value(0)
    
def motion_detect(pin):
    if not led.value():
        ledON()
        sleep(1)

button.irq(trigger=Pin.IRQ_RISING, handler=motion_detect)

while True:
    ledOFF()

