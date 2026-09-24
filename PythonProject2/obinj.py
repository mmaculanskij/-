"""
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
state = 0
period = 1.0

while True:
    GPIO.output(led, state)
    state = not state
    time.sleep(period)
"""

#-------------------------------------------------------------------------


"""
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
botton = 13
GPIO.setup(botton, GPIO.IN)
state = 0

while True:
    if GPIO.input(botton):
        state = not state
        GPIO.output(led, state)
        time.sleep(0.2)

"""

#--------------------------------------------
"""
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
li_sensor = 6
GPIO.setup(li_sensor, GPIO.IN)

while True:
    GPIO.output(led, not GPIO.input(li_sensor))
    time.sleep(0.1)
"""
#-----------------------------------------------------------------------

"""
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
pwm = GPIO.PWM(led, 200)
duty = 0.0
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)
    
    duty += 1.0
    if duty > 100.0:
        duty = 0.0


"""
#--------------------------------------------
"""
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
leds = [24, 22, 23, 27, 17, 25, 12, 16]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
light_time = 0.2

for led in leds:
    GPIO.output(led, 1)
    time.sleep(light_time)
    GPIO.output(led, 0)

for led in reversed(leds):
    GPIO.output(led, 1)
    time.sleep(light_time)
    GPIO.output(led, 0)

"""

#--------------------------------------

"""
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

plus=9
minus=10

GPIO.setup(plus, GPIO.IN)
GPIO.setup(minus, GPIO.IN)

leds=[16, 12, 25, 17, 27, 23, 22, 24]

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

num=0
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
sleep_time=0.2
while True:
    a=GPIO.input(plus)
    b=GPIO.input(minus)
    if a:
        num+=1
        if num>255:
            num=0
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if b:
        num-=1
        if num < 0:
            num=0
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    GPIO.output(leds, dec2bin(num))

"""

#-------------------------
"""
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

plus=9
minus=10

GPIO.setup(plus, GPIO.IN)
GPIO.setup(minus, GPIO.IN)

leds=[16, 12, 25, 17, 27, 23, 22, 24]

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

num=0
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
sleep_time=0.2
while True:
    a=GPIO.input(plus)
    b=GPIO.input(minus)
    if a and b:
        num=255
        print(num, dec2bin(num))
        time.sleep(sleep_time)
        GPIO.output(leds, dec2bin(num))
        continue
    if a:
        num+=1
        if num>255:
            num=0
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if b:
        num-=1
        if num < 0:
            num=0
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    GPIO.output(leds, dec2bin(num))

"""