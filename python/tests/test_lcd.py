# coding: UTF-8
import sys
sys.path.insert(0,'..')

import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from lcd import LCD


if __name__=="__main__":
    from time import sleep
    lcd = LCD()
    while True:
        lcd.displayText("LCD","....")
        sleep(1)
        lcd.displayText("Hello","World")
        sleep(1)