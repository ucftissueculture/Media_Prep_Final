#              Switch Maintenance Test program for                   #
#               Agri-Starts Senior Design Project                    #
#              UCF Senior Design Project - Blue Agave                #
#        Application written by Erik Kantrowitz for Agri-Starts      #

# Control GPIO pins
#   M1 | S0 | S1 | S2 | S3 | S4 |
# | 12 | 07 | 11 | 13 | 15 | 16 |  Board Val
# | 18 | 04 | 17 | 27 | 22 | 23 |  BCM Val

# filling GPIO pins
# | W0 | W1 | W2 | W3 | W4 |
# | 22 | 29 | 31 | 36 | 37 |  Board Val
# | 25 | 05 | 06 | 16 | 26 |  BCM Val

# possible LED indicator
# | L0 |
# | 18 |
# | 24 |
##########################################################################

import signal
import sys
import RPi.GPIO as gpio
import math
from back import Back
#from Integration.backend import back
from time import sleep

back = Back()

#swc = [gpio.input(4), gpio.input(17), gpio.input(22), gpio.input(23), gpio.input(27)]

#x = 0

def run_program():

    print " .   .   .   .    .###.. .   .   .   . "
    sleep(0.25)
    print " .   .   . ..... .#####..... .   .   . "
    print " .   .   . ..##~.?#####Z..##...  .   . "
    sleep(0.25)
    print " .   .   ....###O.#####.####:..  .   . "
    print " .   .   . ..#####,###.#####=..  .   . "
    sleep(0.25)
    print " .   ........######.#.######.......  . "
    print " .   ..I####D,.#####~#####~.D####O.  . "
    sleep(0.25)
    print " .   ...########.###.###.O#######... . "
    print " .   ...+#######O~I#,#Z~########7..  . "
    sleep(0.25)
    print " .   ....=#########,O=O########?..   . "
    print " .   ......########D.O########....   . "
    sleep(0.25)
    print " .   .   ... =#############+...  .   . "
    print " .   .   .   .....#####.......   .   . "
    sleep(0.25)
    print " .   .   .     ....###....   .   .   . "
    print " .   .   .   .   ..###....   .   .   . "
    sleep(0.25)
    print " .   .   .   .   ..### ...   .   .   . "
    print " .   .   .   .   ..### ...   .   .   . "
    sleep(0.25)
    print " .   .   .   .   ..### ...   .   .   . "
    print " .   .   .   .   ..### ...   .   .   . "
    sleep(0.25)
    print " .   .   .   .   ..###....   .   .   . "
    print " .   .   .   .   ..###....   .   .   . "
    sleep(0.25)
    print " .   .   .   .   #######..   .   .   . "
    print " .   .   .   ......?#$....   .   .   . "
    sleep(0.25)
    print " .   .   .   . .....#.....   .   .   . "
    print " .   .   .   .   .  O.   .   .   .   . "
    sleep(0.25)
    print "               Agri-Starts             "
    print "\n\n\r"
    print("       Switch Testing Program is running.          ")
    print(" ------------------------------------------------  ")
    print(" To check if a switch is working correctly please  ")
    print("  manually press the two switches simultaneously   ")
    print(" ------------------------------------------------  ")
    print("      To exit the program press control-c          ")



    while 1:
        # swc = [gpio.input(4), gpio.input(17), gpio.input(22), gpio.input(23), gpio.input(27)]
	x=0
        if gpio.input(4):
	    print "Switch 1 pressed"
           # if x == 0:
            #    print "\rswitch 1 Pressed"
             #   sleep(0.5)
              #  x = 1
          #  else:
           #     x = 1

        # elif swc[1] == 0:
        #     print "switch 2 Pressed"
        #
        # elif swc[2] == 0:
        #     print "switch 3 Pressed"
        #
        # elif swc[3] == 0:
        #     print "switch 4 Pressed"
        #
        elif gpio.input(27):
	    print "Switch 5 Pressed"
           # if x == 0:
            #    print "\rswitch 5 Pressed"
             #   sleep(0.5)
              #  x = 1
           # else:
            #    x = 1

        else:
            print "no switches pressed "
	    print "switch 1 reads: ", gpio.input(4)
	    print "switch 5 reads: ", gpio.input(27)
           # sleep(1)
           # x = 0

def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)

    try:
        if raw_input("\nReally quit? (y/n) ").lower().startswith('y'):
            gpio.cleanup()
            sys.exit(1)

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        gpio.cleanup()
        sys.exit(1)

    # restore the exit gracefully handler here
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    # store the original SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
    run_program()
