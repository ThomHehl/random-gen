# Example Servo Code
# Control the angle of a
# Servo Motor with Raspberry Pi

# free for use without warranty
# www.learnrobotics.org

import RPi.GPIO as GPIO
from time import sleep

servoCTL = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoCTL, GPIO.OUT)

pwm = GPIO.PWM(servoCTL, 50)
pwm.start(0)

def setAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(servoCTL, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servoCTL, False)
    pwm.ChangeDutyCycle(duty)


count = 0
numLoops = 2

while count < numLoops:
    print("set to 0-deg")
    setAngle(0)
    sleep(1)

    print("set to 90-deg")
    setAngle(90)
    sleep(1)

    print("set to 180-deg")
    setAngle(180)
    sleep(1)

    count = count + 1

pwm.stop()
GPIO.cleanup()