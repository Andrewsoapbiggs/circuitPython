import time
import board
import pulseio
import touchio
import neopixel
from adafruit_motor import servo

touch_1 = board.A0
#sets A0 to touch one
touch_2 = board.A1
#sets A1 to touch 2
pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
#sets the frequency and sets up duty cicle to go out of A2 with pulsie io and PWM
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
my_servo = servo.Servo(pwm)
touch1 = touchio.TouchIn(touch_1)
touch2 = touchio.TouchIn(touch_2)
angle = 0

while True:
    if touch1.value:
        print("wow!")
    #for angle in range(0, 180, 5):
        if angle < 180:
            angle+=10
        my_servo.angle = angle
        time.sleep(0.05)
    if touch2.value:
        print("spicy!")
        if angle > 0:
            angle-=10
        my_servo.angle = angle
        time.sleep(0.05)
    #for angle in range(0, 180, 5):
    #    my_servo.angle = angle
    #    time.sleep(0.05)
    #for angle in range(180, 0, -5):
     #   my_servo.angle = angle
     #   time.sleep(0.05)