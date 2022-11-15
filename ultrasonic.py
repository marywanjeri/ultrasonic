from machine import Pin
import time
trigger = Pin(3, Pin.OUT)
echo = Pin(4, Pin.IN)
def ultra():
   trigger.low()
   time.sleep_us(3)
   trigger.high()
   time.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = time.ticks_us()
   while echo.value() == 1:
       signalon = time.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   print("The distance from the object is ",distance,"cm")
while True:
   ultra()
   time.sleep(1)
