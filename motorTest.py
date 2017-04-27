# pwm test for motor control

# inputs for easy control
import tty
import sys
import termios

# imports for pwm use
import wiringpi
import time

# setting up the GPIO pin for pwm and seting the frequency
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# pwm frequency in Hz: 19,200,000 / pwmSetClock / pwmSetRange
# 19,200,000 / 10 / 1000 = 1920
wiringpi.pwmSetClock(10)
wiringpi.pwmSetRange(1000)



# loop-de-loop input into stdin 'r' to run the motor 's' to stop it
while 1:
    x=sys.stdin.read(1)
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

    if x == 'f':
        wiringpi.pwmWrite(18, 1000)
