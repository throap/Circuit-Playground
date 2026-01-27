import time
import board
import neopixel


pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

while True:
    pixels[2]=(255, 0, 0) #flash red for every other rgb light
    pixels[0]=(255, 0, 0)
    pixels[4]=(255, 0, 0)
    pixels[6]=(255, 0, 0)
    pixels[8]=(255, 0, 0)
    time.sleep(0.5)
    pixels.fill((225, 100, 100)) #make the default color pink-ish
    time.sleep(0.5)
