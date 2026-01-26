import board
import digitalio
import time
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL,5)
led.brightness = 0.1
print(dir(led))
while True:
    
    led[0] = (255,100,100)
    time.sleep(.5)
    led[0] = (0,0,0)
    time.sleep(.5)
    led[0] = (100,255,100)
    time.sleep(.5)
    led[0] = (0,0,0)
    time.sleep(.5)
    led[0] = (100,100,255)
    time.sleep(.5)
    led[0] = (0,0,0)
    time.sleep(.5)
