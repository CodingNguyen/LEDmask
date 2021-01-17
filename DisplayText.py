from PIL import Image, ImageFont, ImageDraw
import board
import neopixel
import time

width = 16 # matrix width
height = 8 # matrix height
color = (255,255,255) # white

#use for the flex grid
def getIndex(x, y):
    x = width-x-1
    if x % 2 != 0: # check for odd or even row
        return (x*8)+y # even columns go down
    else:
        return (x*8)+(7-y) # odd rows go up

# reading the output of SpeechToText.py
# default to "Hello world" if error occurs
try:
    file = open("speechOutput.txt")
    text = file.read()
    file.close()
except:
    text = "Hello world"

# initialize LED matrix
pixelPin = board.D21 # Data output on pin D21
numPixels = 128 # for two 16x16 matrices
ORDER = neopixel.GRB # color order of LEDs

pixels = neopixel.NeoPixel(pixelPin, numPixels, brightness=.1, auto_write=False, pixel_order=ORDER)

# turn off LEDs
pixels.fill((0,0,0))
pixels.show()
time.sleep(.0001)

# initialize font
textFont = ImageFont.truetype("5x7_practical.ttf", 16)
textWidth, textHeight = textFont.getsize(text)

# initialize PIL image for text
image = Image.new('P', (textWidth + width * 2, height), 0)
draw = ImageDraw.Draw(image)

# Draw the text into the image
draw.text((8, -1), text, font=textFont, fill=255)
image.save("imageOutput.png")

offset = 0 # allows scrolling effect

# Display image onto LED matrix
while True:
    # iterate through each pixel
    for x in range(width):
        for y in range(height):
            # check if pixel is white, otherwise LED is turned off
            if image.getpixel((x + offset, y)) == 255:
                pixels[getIndex(x, y)] = color
            else:
                pixels[getIndex(x, y)] = (0, 0, 0)
    offset += 1 # shift text left 1 column
    if offset + width > image.size[0]: # reset offset at end of image
        offset = 0

    # display 
    pixels.show()
    time.sleep(.025)
