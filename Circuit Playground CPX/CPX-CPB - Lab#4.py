import time
import board
import neopixel
color = (100,225,225)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

while True:
    for i in range (10):
        pixels[i] = color 
        time.sleep(0.2)
        pixels.fill((0, 0, 0))
