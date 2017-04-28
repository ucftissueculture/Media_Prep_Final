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

    # turns motor on instantly at 60%
    def motorOn(self):
        wiringpi.pwmWrite(18, 800)
        motorState = 1

    # This function should allow running a motor on a different pin
    def motor(self, pin, speed):
        wiringpi.pwmWrite(pin, speed)
        motorState = 1

    # stops motor on instantly
    def motorOff(self):
        wiringpi.pwmWrite(18, 0)
        motorState = 0

    def motorSpeed(self, speed):
	wiringpi.pwmWrite(18, speed)


    ## this is mostly for testing, but an indicator LED can be added

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

    def switchTest(self):

        print("       Switch Testing Program is running.          ")
        print(" ------------------------------------------------  ")
        print(" To check if a switch is working correctly please  ")
        print("  manually press the two switches simultaneously   ")
        print(" ------------------------------------------------  ")
        print("      To exit the program press control-c          ")



        while 1:
           
            if gpio.input(4):
                print "Switch 1 pressed"


           ## To add more switches simply add another on of these replacing '17' with
           ## the gpio pin that the switch is connected to.
           # elif gpio.input(17):
               # print "Switch 2 Pressed"

            elif gpio.input(27):
                print "Switch 5 Pressed"


            else:
                print "no switches pressed "
                print "switch 1 reads: ", gpio.input(4)
                print "switch 5 reads: ", gpio.input(27)



    def motorTest(self):

        print("        Motor Testing Program is running.          ")
        print(" ------------------------------------------------  ")
        print(" Enter 'r' to run the motor, a number 1 - 9 to run ")
        print("       at a different speed, and 's' to stop.      ")
        print(" ------------------------------------------------  ")
        print("      To exit the program press control-c          ")
            

        while 1:
            x = sys.stdin.read(1)
            
            if x == 'r':
                #motor on
                wiringpi.pwmWrite(18, 600)
            if x == 's':
                #motor off
                wiringpi.pwmWrite(18, 0) 

            if x == '1':
                wiringpi.pwmWrite(18, 100)

            if x == '2':
                wiringpi.pwmWrite(18, 200)

            if x == '3':
                wiringpi.pwmWrite(18, 300)

            if x == '4':
                wiringpi.pwmWrite(18, 400)

            if x == '5':
                wiringpi.pwmWrite(18, 500)

            if x == '6':
                wiringpi.pwmWrite(18, 600)

            if x == '7':
                wiringpi.pwmWrite(18, 700)

            if x == '8':
                wiringpi.pwmWrite(18, 800)

            if x == '9':
                wiringpi.pwmWrite(18, 900)



    def fillTest(self):

        print("       Filling Testing Program is running.            ")
        print(" ---------------------------------------------------- ")
        print(" Enter 'f' for filling, 'o' to open, and 's' to close ")
        print(" ---------------------------------------------------  ")
        print("      To exit the program press control-c             ")

        while 1:
            x=sys.stdin.read(1)
            if x == 'f':
                back.filling()
            if x == 's':
                gpio.output(26, 1)
            if x == 'o':
                gpio.output(26, 0)

    def alignTest(self):
        print("        Alignment Testing Program is running.         ")
        print(" ---------------------------------------------------- ")
        print(" Run the tray through the system to check the tray    ")
        print("    alignment, the tray will stop under filling,      ")
        print("        but will not open the filling valves          ") 
        print(" ---------------------------------------------------  ")
        print("      To exit the program press control-c             ")
        while 1:
            if gpio.input(4):
                back.motorOff()
                print "TRIGGER WARNING:  Filling switch triggered"
                sleep(0.25)
                if gpio.input(4):
                    back.motorOn()
                    sleep(3.2)			# If the jars are not alligned, change this value to adjust
                    back.motorOff()
                    sleep(1.25)
                    sleep(2)

            if gpio.input(27):
                back.motorOff()
                print "TRIGGER WARNING: End switch triggered"
                sleep(0.1)

            else:
                back.motorOn()
                print "running"
                sleep(0.1)

