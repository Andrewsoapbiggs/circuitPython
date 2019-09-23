import time
# import math
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import CursorMode
photo = DigitalInOut(board.D8)

photo.direction = Direction.INPUT
photo.pull = Pull.UP
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)
photoState = True
oldPhoto = True
value = 0

while True:
    photoState = photo.value

    if  photoState and not oldPhoto:
        value = value + 1
        lcd.set_cursor_pos(1, 0)
        lcd.print(str(value))

    else:
        lcd.set_cursor_pos(1, 0)
        lcd.print(str(value))

    oldPhoto = photoState