import board
# this imports the board so Python and metro can interact
import time
# this allows python and time to interact
import pulseio
#this adds PWN to be used in the code
from board import *

led = pulseio.PWMOut(board.D8, frequency=5, duty_cycle=0)
#this sets verible names it sets the PWN pin to 8
while True:
    for i in range(100):
        #the base range value for I is set to 100 and I is established
        if i < 5:
            led.duty_cycle = int(i * 4 * 6000/ 6)
            # i = number that is current plus the math that was just added / starts 2000
        else:
            led.duty_cycle - 60 - int((i - 20) * 4 * 6000/ 6)

        time.sleep(1)