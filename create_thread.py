import _thread
from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)
#led = Pin(2, Pin.OUT) #for esp32

def blinkLED():
    led.value(0)
    sleep(1)
    led.value(1)
    sleep(1)
    
def blinkforever():
    while True:
        blinkLED()
    
_thread.start_new_thread(blinkforever, ())

while True:
    print("Hello World")
    sleep(2)

