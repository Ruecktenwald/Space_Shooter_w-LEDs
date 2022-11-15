from rpi_ws281x import *
from rpi_ws281x import Color
import time


LED_COUNT = 40
LED_PIN =18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 200
LED_INVERT = False
LED_CHANNEL = 0


strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

for x in range(0, LED_COUNT):
    strip.setPixelColor(x, Color(0,0,255))
    strip.show() 


def shoot_blaster():
    LED_BRIGHTNESS = 255
    for x in range(0, 40):
        strip.setPixelColor(x, Color(0,255,0))
    strip.show()
    time.sleep(0.02)
    LED_BRIGHTNESS = 200
    for x in range(0, 40):
        strip.setPixelColor(x, Color(0,0,255))
    strip.show()
        