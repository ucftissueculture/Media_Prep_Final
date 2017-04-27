#                  Backend Implementation Class                      #
#              UCF Senior Design Project - Blue Agave                #
#        Application written by Erik Kantrowitz for Agri-Starts      #


# Control GPIO pins
#   M1 | S0 | S1 | S2 | S3 | S4 |
# | 12 | 07 | 11 | 13 | 15 | 16 |  Board Val
# | 18 | 04 | 17 | 27 | 22 | 23 |  BCM Val

# filling GPIO pins
# | W0 | W1 | W2 | W3 | W4 |
# | 22 | 29 | 31 | 36 | 37 |  Board Val
# | 05 | 06 | 16 | 25 | 26 |  BCM Val

# possible LED indicator
# | L0 |
# | 18 |
# | 24 |



# these imports are for controlling the GPIO pins and pwm
import RPi.GPIO as gpio
import wiringpi
from time import sleep

class Back(object):

    def __init__(self):

        # setting up the GPIO settings for the pwm
        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
        wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

        # pwm frequency in Hz: 19,200,000 / pwmSetClock / pwmSetRange
        # 19,200,000 / 10 / 1000 = 1920
        wiringpi.pwmSetClock(10)
        wiringpi.pwmSetRange(1000)

        # sets gpio to BCM pinout
        gpio.setmode(gpio.BCM)

        # gpio.setup(0, gpio.IN, pull_up_down=gpio.PUD_UP)
        gpio.setup(4, gpio.IN, pull_up_down=gpio.PUD_UP)
        gpio.setup(27, gpio.IN, pull_up_down=gpio.PUD_UP)

        # this variable is for making sure only one press is logged
        # when a switch is pressed
        switchState = 0
        motorState = 1          #Motor on initially

        # initialization for filling
        gpio.setup(26, gpio.OUT)

########################END OF __INIT__########################

    # a few motor controll functions that might be usefull

    # currently all of these motor functions are set to only run
    # the motor connected to pin 18, for final deployment
    # this can be made better by allowing a second argument
    # that takes in an int and replaces 18 in all the motor
    # methods with that int
    # ex:    def motorOn(self, n):
    #           wiringpi.pwmWrite(n, 600)

    # turns motor on instantly at 60%
    def motorOn(self):
        wiringpi.pwmWrite(18, 800)
        motorState = 1

    def motor(self, pin, speed):
        wiringpi.pwmWrite(pin, speed)
        motorState = 1

    # stops motor on instantly
    def motorOff(self):
        wiringpi.pwmWrite(18, 0)
        motorState = 0

    def motorSpeed(self, speed):
	wiringpi.pwmWrite(18, speed)

    ## for whatever reason the motorRampDown function was not
    ## working when trying to ramp down on exit.

    ## during testing the motor stop function didn't seem as
    ## abrupt as I worried it might be so the ramp up & down
    ## methods might not be worth having

    # # ramps motor down from 60% to off with 10% increments
    # def motorRampDown(self):
    #     for i in range(800, 0, 10):
    #         wiringpi.pwmWrite(18, i)
    #
    # # ramps motor up from off to 60% with 10% increments
    # def motorRampUp(self):
    #     for i in range(o, 800, 10):
    #         wiringpi.pwmWrite(18, i)




    ## this is mostly for testing, but an indicator LED can be used
    ## in final release
    # function to control an LED, it takes in the state to change
    # the LED to for example ledState(on), turns the LED on
    def ledState(self, state):
        state = state.lower()
        if state == "on":
            ledOn = gpio.output(24, 1)      # led on
        if state == "off":
            ledOff = gpio.output(24, 0)     # led off

    def ledBlink(self):
        gpio.output(24, 0)
        sleep(1/10)
        gpio.output(24, 1)
        gpio.output(24, 0)
        sleep(1/10)
        gpio.output(24, 1)

    def filling(self):
        # ON = 0
        # OFF = 1
        # duration = 4

	
	
        gpio.output(26, 0)
        sleep(4)		# To change the duration that the filling valves are open change this value to the required seconds you want open 
        gpio.output(26, 1)
	sleep(2)
