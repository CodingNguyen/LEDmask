from PIL import Image, ImageFont, ImageDraw
import board
import neopixel
import time

width = 16 # matrix width
height = 8 # matrix height
color = (255,255,255) # white

# initialize LED matrix
pixelPin = board.D21 # Data output on pin D21
numPixels = 128 # for two 16x16 matrices
ORDER = neopixel.GRB # color order of LEDs

pixels = neopixel.NeoPixel(pixelPin, numPixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

# turn off LEDs
pixels.fill((0,0,0))
pixels.show()
time.sleep(.0001)