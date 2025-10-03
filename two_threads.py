import _thread
from machine import Pin
from time import sleep

toggle = False

led = Pin(25, Pin.OUT)
#led = Pin(2, Pin.OUT) # for esp32
lock = _thread.allocate_lock()

def ledON():
    led.value(1)
def ledOFF():
    led.value(0)
    
# thread for OFF
def switchOFF():
    global toggle
    while True:
        lock.acquire()
        if toggle:
            ledOFF()
            toggle=False
        sleep(1)
        lock.release()
        
_thread.start_new_thread(switchOFF, ())

# thread for ON 
while True:
    lock.acquire()
    if not toggle:
        ledON()
        toggle=True
    sleep(1)
    lock.release()

