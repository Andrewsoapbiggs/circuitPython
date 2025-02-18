import time
# import math
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import CursorMode
button = DigitalInOut(board.D8)

button.direction = Direction.INPUT
button.pull = Pull.UP
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)
buttonState = True
oldButton = True
value = 0

while True:
    buttonState = button.value
    print(oldButton, buttonState)

    if not button.value and oldButton:
        value = value + 1
        lcd.set_cursor_pos(0, 0)
        lcd.print("Now Pressed")
        lcd.set_cursor_pos(1, 0)
        lcd.print(str(value))

    else:
        lcd.set_cursor_pos(0, 0)
        print(value)
        lcd.print("Not Pressed   ")
        lcd.set_cursor_pos(1, 0)
        lcd.print(str(value))

    lcd.set_cursor_mode(CursorMode.LINE)
    time.sleep(0.1)

    oldButton = buttonState