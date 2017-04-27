import signal
import sys
import RPi.GPIO as gpio
from back import Back
from time import sleep

back = Back()

def run_program(): 
    print "Enter 'f' for filling, 'o' to open, and 's' to close"
    while 1:
        x=sys.stdin.read(1)
        if x == 'f':
            back.filling()
        if x == 's':
            gpio.output(26, 1)
        if x == 'o':
            gpio.output(26, 0)


def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)

    try:
        if raw_input("\nReally quit? (y/n) ").lower().startswith('y'):
            back.motorOff()
            sys.exit(1)

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        back.motorOff()
        sys.exit(1)

    # restore the exit gracefully handler here
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    # store the original SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
    run_program()
