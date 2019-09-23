#Andrew D`Alessio
#9/23/2019
#NeoPixel Distance
import time
import board
import adafruit_hcsr04
import neopixel
import simpleio
R = 0
B = 0
G = 0
sonarValue = 0
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D4, echo_pin=board.D5)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=.1)


while True:
    try:
        sonarValue = sonar.distance
#you must use  SonarValue or you will be asking for the distance 3 times  every .01 a second which can not be handeld
        print(sonarValue)
    except RuntimeError:
        print("Retrying!")
        #if the system faulters instead of crashing is retrys the system
        pass

    R = simpleio.map_range(sonarValue, 5, 20, 255, 0)
#controls Red Value by taking value R and when its between 5-20 you are going from high red to low red
    G = simpleio.map_range(sonarValue, 20, 35, 0, 255)
#controls Green Value Same as above
    B = simpleio.map_range(sonarValue, 5, 20, 0, 255)
#controls Blue value Same as above
    dot.fill((int(R), int(G), int(B)))
#you have to convert  all the numbers to ints before sending them or else it crashes due to a float value error

time.sleep(.01)