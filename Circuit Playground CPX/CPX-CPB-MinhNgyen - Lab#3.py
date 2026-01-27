import time
import board
import neopixel


pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

while True:
    pixels[0]=(255, 0, 0)
    pixels[1]=(225, 100, 0)
    pixels[2]=(225, 100, 100)
    pixels[3]=(100, 225, 0)
    pixels[4]=(100, 225, 100)
    pixels[5]=(0, 225, 100)
    pixels[6]=(0, 0, 225)
    pixels[7]=(0, 100, 225)
    pixels[8]=(0, 1, 225)
    pixels[9]=(100, 100, 225) #rainbow colors (or a lot of different colors) 
    time.sleep(0.5)
    pixels.fill((0, 0, 0)) #flahes nothing after rainbow, making it blink rainbow)
    time.sleep(0.5)
