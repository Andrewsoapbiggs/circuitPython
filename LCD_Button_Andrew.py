import time
import math
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import CursorMode
button = DigitalInOut(board.D8)

button.direction = Direction.INPUT
button.pull = Pull.UP
lcd = LCD(I2CPCF8574Interface(0x27), num_rows=4, num_cols=20)

lcd.set_cursor_pos(1, 4)
lcd.print("Here I am")
#while True:
#    lcd.print("Hello")
#    if not button.value:
#    lcd.print("Hello")
#    else:
#        print("no")
#    time.sleep(0.1)